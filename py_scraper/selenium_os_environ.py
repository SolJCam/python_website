import os, pdb
from selenium import webdriver

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def choose_os():
    try:
        if os.environ["SOLS_MAC"]:
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--test-type")
            options.add_argument("--headless")

            # Chrome Driver options
            # options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            # drive_path = os.path.join(d, 'drivers/chromedriver94')
            options.binary_location = "/Applications/Google Chrome 2.app/Contents/MacOS/Google Chrome"
            drive_path = os.path.join(d, 'drivers/chromedriver')

            # Instanciate WebDriver
            driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path)

            # # Chromium Driver backup options
            # options.binary_location = "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
            # options.binary_location = "/Applications/Chromium.app/Contents/MacOS/Chromium"
            # drive_path = os.path.join(d, 'drivers/chromedriver81')

            # # Driver for testing (Includes log)
            # driver = webdriver.Chrome(chrome_options=options,executable_path=drive_path,service_args=["--verbose", "--log-path=selchrome.log"])

            return driver
    except Exception as e:
        # Chrome/Selenium configuration for Heroku
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        driver = webdriver.Chrome(chrome_options=options,executable_path=os.environ.get('CHROMEDRIVER_PATH'))       # to update driver version: heroku config:set CHROMEDRIVER_VERSION=

        return driver
