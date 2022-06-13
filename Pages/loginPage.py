from Locator.loginLocator import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_with_halo_acc(self):
        print('Login with haha lolo account')
        login_halo_acc = self.driver.find_element_by_id(get_login_with_halo_btn_id())
        login_halo_acc.click()

    def click_login_with_anonymous_acc(self):
        print('Login with anonymous account')
        anonymous_btn = self.driver.find_element_by_id(get_anonymous_btn_id())
        anonymous_btn.click()

    def enter_username(self, username):
        print("Enter user name")
        username_input = self.driver.find_element_by_id(get_username_id())
        username_input.clear()
        username_input.send_keys(username)

    def enter_pwd(self, pwd):
        print("Enter password")
        pwd_input = self.driver.find_element_by_id(get_pwd_id())
        pwd_input.clear()
        pwd_input.send_keys(pwd)

    def click_login(self):
        print("Click login button")
        login_btn = self.driver.find_element_by_xpath(get_login_btn_xpath())
        login_btn.click()

    def click_continue(self):
        print("Click login continue")
        login_continue_btn = self.driver.find_element_by_id(get_login_continue_btn_id())
        login_continue_btn.click()

    def enter_phone_number(self, phone_number):
        print("Enter phone number")
        phone_number_input = self.driver.find_element_by_id(get_input_phone_number_id())
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)

    def click_login_anonymous_start_btn(self):
        print("Start")
        anonymous_start_btn = self.driver.find_element_by_id(get_anonymous_start_btn_id())
        anonymous_start_btn.click()

    def enter_opt(self, opt):
        print("Enter Opt")
        opt_input = self.driver.find_element_by_xpath(get_opt_input_xpath())
        opt_input.clear()
        opt_input.send_keys(opt)

    def enter_pin(self, pin):
        print("Enter Pin")
        pin_input = self.driver.find_element_by_xpath(get_pin_input_xpath())
        pin_input.clear()
        pin_input.send_keys(pin)

    def noti_login_fail(self):
        login_fail = self.driver.find_element_by_xpath(get_noti_login_fail()).text
        print(login_fail)

    def noti_not_username(self):
        not_username = self.driver.find_element_by_xpath(get_noti_not_username()).text
        print(not_username)

    def noti_not_password(self):
        not_password = self.driver.find_element_by_xpath(get_noti_not_password()).text
        print(not_password)

