from Pages.loginPage import LoginPage
from Pages.logoutPage import LogoutPage
from Utils.customChromeDriver import custom_chrome_driver
import unittest
import time
from Utils.infoLogin import get_info_login
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


class LoginTestInChrome(unittest.TestCase):


    def setUp(self) -> None:
        self.driver = custom_chrome_driver()
        info = get_info_login()
        self.url = info[0]
        self.sheet = info[1]
        self.pin = info[2]
        self.username = None
        self.pwd = None

    def test_login_success(self):
        print("Đăng nhập đúng username và password")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(1,0)
        self.pwd = self.sheet.cell_value(1,1)
        time.sleep(2)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(2)
        logout = LogoutPage(self.driver)
        logout.click_avatar()
        logout.click_logout()
        logout.click_ok()
        login.click_login_with_halo_acc()
        logout.click_not_account()

    def test_login_u_p_fail(self):
        print("Đăng nhập với username và password sai")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(2, 0)
        self.pwd = self.sheet.cell_value(2, 1)
        time.sleep(1)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        login.noti_login_fail()

    def test_login_not_u_p(self):
        print("Đăng nhập không có username và password")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        time.sleep(1)
        try:
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        print("Notification")
        login.noti_not_username()
        login.noti_not_password()

    def test_login_not_p(self):
        print("Đăng nhập không mật khẩu")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(4, 0)
        self.pwd = self.sheet.cell_value(4, 1)
        time.sleep(1)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        print("Notification")
        login.noti_not_password()

    def test_login_not_u(self):
        print("Đăng nhập không username")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(5, 0)
        self.pwd = self.sheet.cell_value(5, 1)
        time.sleep(1)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        print("Notification")
        login.noti_not_username()

    def test_login_p_fail(self):
        print("Đăng nhập với mật khẩu sai")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(6, 0)
        self.pwd = self.sheet.cell_value(6, 1)
        time.sleep(1)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        print("Notification")
        login.noti_login_fail()

    def test_login_u_fail(self):
        print("Đăng nhập với username sai")
        self.driver.get(self.url)
        login = LoginPage(self.driver)
        login.click_login_with_halo_acc()
        self.username = self.sheet.cell_value(7, 0)
        self.pwd = self.sheet.cell_value(7, 1)
        time.sleep(1)
        try:
            login.enter_username(self.username)
            login.enter_pwd(self.pwd)
            login.click_login()
            login.click_continue()
            login.enter_pin(self.pin)
        except StaleElementReferenceException as stale:
            print(stale)
            pass
        except NoSuchElementException as no_element:
            print(no_element)
            pass
        time.sleep(1)
        print("Notification")
        login.noti_login_fail()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()