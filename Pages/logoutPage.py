from Locator.logoutLocator import *


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_avatar(self):
        click_avt = self.driver.find_element_by_xpath(get_avatar_button_xpath())
        click_avt.click()

    def click_logout(self):
        click_lo = self.driver.find_element_by_xpath(get_logout_button_xpath())
        click_lo.click()

    def click_ok(self):
        click_ok_lg = self.driver.find_element_by_id(get_ok_button_id())
        click_ok_lg.click()

    def click_not_account(self):
        print("Not me")
        not_account = self.driver.find_element_by_xpath(get_not_account())
        not_account.click()

    def click_avatar_not_img(self):
        print("Click avatar not image")
        avatar_not_img = self.driver.find_element_by_xpath(get_avatar_not_img())
        avatar_not_img.click()