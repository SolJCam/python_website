import os, pdb
from selenium import webdriver

def choose_os():
    try:
        if os.environ["SOLS_MAC"]:
            driver = webdriver.Chrome()
            return driver
        
    except Exception as e:
        # Chrome/Selenium configuration for Heroku
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        driver = webdriver.Chrome(options=options,executable_path=os.environ.get('CHROMEDRIVER_PATH'))       # to update driver version: heroku config:set CHROMEDRIVER_VERSION=

        return driver
