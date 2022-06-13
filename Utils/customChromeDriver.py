from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def custom_chrome_driver():
    opt = Options()
    driver = webdriver.Chrome("../Driver/ChromeDriver/chromedriver", options=opt)

    driver.implicitly_wait(30)
    driver.maximize_window()

    print('Open chrome browser')
    return driver
