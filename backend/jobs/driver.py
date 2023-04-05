import environ
from django.conf import settings
from selenium import webdriver

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
WINDOW_SIZE = "1200x1000"

class Browser(webdriver.Chrome):
    timeout = 30

    def __init__(self):
        
        # Adds the executable folder to PATH so that chromedriver is available
        path_bin = str(settings.BASE_DIR / 'bin')
        
        env = environ.Env()
        PATH = env('PATH', default=path_bin)
        
        # Customise Chrome options
        chrome_options = webdriver.ChromeOptions()
        
        # Allows you to launch Chrome without a window
        chrome_options.add_argument('--headless')
        
        # Google recommends this option
        chrome_options.add_argument("--no-sandbox")
        
        # Fixing issues with Docker memory
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Allows you to customise the USER_AGENT
        chrome_options.add_argument(f"user-agent={USER_AGENT}")
        
        # Allows you to change the size of the window
        chrome_options.add_argument(f"window-size={WINDOW_SIZE}")
        
        super().__init__(chrome_options=chrome_options)