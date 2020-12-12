from selenium import webdriver

DIRECTORY='reports'
NAME='mobile'
CURRENCY='₹'
MIN_PRICE='10000'
MAX_PRICE='20000'
FILTERS={
        'min':MIN_PRICE,
        'max':MAX_PRICE
}
BASE_URL="https://www.amazon.in/"

#opeing the browser

def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver',chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate_errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')