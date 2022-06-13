from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def custom_firefox_driver():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path="../Driver/FirefoxDriver/geckodriver.exe", options=options)

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open Firefox browser')
    return driver
