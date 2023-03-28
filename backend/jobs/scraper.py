from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import random


def get_jobs_data(job_title, location, num_pages=1):
    # create chrome driver instance
    DRIVER_PATH = './chromedriver'
    options = webdriver.ChromeOptions()
    # set incognito mode
    options.add_argument('- incognito')
    # create new instance of chrome in incognito mode
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    base_url = "https://www.indeed.com/"
    job_data = []
    timeout = 25

    # get the url and wait for the page to load
    driver.get(base_url)
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
        job_posts = soup.find_all('table', class_='jobCard_mainContent')

        for job_post in job_posts:
            job_link = job_post.find('a', class_='jcs-JobTitle')['id']
            job_id = job_link.split('_')[1]
            job_url = f"https://www.indeed.com/jobs?q=django&l=Malaysia&from=searchOnHP&vjk={job_id}"

            title = job_post.find('a', class_='jcs-JobTitle').text.strip()
            company = job_post.find('span', class_='companyName').text.strip()
            location = job_post.find('div', class_='companyLocation').text.strip()
            salary = job_post.find('div', class_='attribute_snippet')
            salary = salary.text.strip() if salary else None

            job_data.append({
                'id': job_id,
                'title': title,
                'company': company,
                'location': location,
                'salary': salary,
                'job_url': job_url
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

                print(job['description'])

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
                print(f"Timed out waiting for job description to load, skipping job (jobId: {job.id})...")
                # drop job from list
                job_data.remove(job)

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
