import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.conf import settings
from bs4 import BeautifulSoup
import time
import random

# from driver import Browser


def get_jobs_data(job_title, location, num_pages=1):
    
    if settings.DEBUG:
        # create chrome driver instance
        DRIVER_PATH = './chromedriver'
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        
    else:
        chrome_remote_url = settings.CHROME_DRIVER_REMOTE_URL
        
        options = webdriver.ChromeOptions()
        options.add_argument(' - incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities.update(options.to_capabilities())
        
        driver = webdriver.Remote(chrome_remote_url, capabilities)
        
        print("Remote driver is created")
        
    


    base_url = "https://www.indeed.com/"
    job_data = []
    timeout = 50

    # get the url and wait for the page to load
    driver.get(base_url)
    time.sleep(5)
    print(driver.page_source)
    print(f"Getting {base_url}...")
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "text-input-what")))
    except TimeoutException:
        print("Timed out waiting for initial page to load")
        driver.quit()

    print("Page loaded")

    # Search job title and location
    search_title = driver.find_element(By.ID, "text-input-what")
    search_title.clear()
    search_title.send_keys(job_title)

    search_location = driver.find_element(By.ID, "text-input-where")
    search_location.clear()
    search_location.send_keys(location)
    search_location.send_keys(Keys.RETURN)

    # wait for search results to load
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jobsearch-ResultsList")))
    except TimeoutException:
        print("Timed out waiting for search results to load")
        driver.quit()

    # Scrape job data
    for page_number in range(1, num_pages + 1):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_posts_main = soup.find_all('table', class_='jobCard_mainContent')
        job_posts_shelf = soup.find_all('table', class_='jobCardShelfContainer')
        

        for (job_post_main, job_post_shelf) in zip(job_posts_main, job_posts_shelf):
            job_link = job_post_main.find('a', class_='jcs-JobTitle')['id']
            job_id = job_link.split('_')[1]
            job_url = f"https://www.indeed.com/jobs?q=django&l=Malaysia&from=searchOnHP&vjk={job_id}"

            title = job_post_main.find('a', class_='jcs-JobTitle').text.strip()
            company = job_post_main.find('span', class_='companyName').text.strip()
            location = job_post_main.find('div', class_='companyLocation').text.strip()
    
            
            # get data from job shelf if it exists
            # date is in format of "Posted 1 day ago" or "Active 1 day ago"
            # remove the "Posted" or "Active" part
            date = job_post_shelf.find('span', class_='date')
            date = date.text.strip() if date else None

            job_data.append({
                'id': job_id,
                'title': title,
                'company': company,
                'location': location,
                'job_url': job_url,
                'date': date
            })

            print(job_data)

        # Scrape job descriptions
        for job in job_data:
            driver.get(job['job_url'])
            try:
                WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, "jobDescriptionText")))
                job_description_soup = BeautifulSoup(driver.page_source, 'html.parser')
                job_description = str(job_description_soup.find('div', id='jobDescriptionText'))
                job['description'] = job_description


                # Avoid bot detection
                sleep_time = random.uniform(0.5, 1.0)
                time.sleep(sleep_time)

                driver.back()
                try:
                    WebDriverWait(driver, timeout).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.jobsearch-ResultsList")))
                except TimeoutException:
                    print("Timed out waiting for search results to load after navigating back")
                    # delete all jobs that have been scraped their descriptions
                    for job in job_data:
                        if 'description' in job:
                            pass
                        else:
                            job_data.remove(job)
                    driver.quit()
                    break

            except TimeoutException:
                print(f"Timed out waiting for job description to load, skipping job...")
                # drop job from list
                job_data.remove(job)
                # go back to search results page for next job
                driver.back()

        if num_pages > 1 and page_number < num_pages:
            try:
                pagination_links = driver.find_elements(By.CSS_SELECTOR, 'nav[aria-label="pagination"] a')
                next_link = None

                for link in pagination_links:
                    if link.get_attribute('data-testid') == f"pagination-page-{page_number + 1}":
                        next_link = link
                        break

                if next_link is None:
                    break

                next_link.click()

            except:
                print("Was not able to navigate to another page")
                break

    return job_data
