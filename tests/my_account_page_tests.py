"""
Created on February 16, 2020

@author: Mark Zirpoli

This module contains the unit tests for My Account page
"""

from pages.sign_in_page import SignInPage
from pages.my_account_page import MyAccountPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class MyAccountPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sign_in = SignInPage(self.driver)
        self.sign_in.click_sign_in_menu_button()
        self.sign_in.input_email_address_textbox("test1940@gmail.com")
        self.sign_in.input_password_textbox("abcd1234")
        self.sign_in.click_sign_in_button()
        self.my_account = MyAccountPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_name_of_your_friend_textbox(self):
        self.my_account.click_order_history_and_details_button()

    @unittest.skip("pass")
    def test_click_my_wishlists_button(self):
        self.my_account.click_my_wishlists_button()

    @unittest.skip("pass")
    def test_click_my_credit_slips_button(self):
        self.my_account.click_my_credit_slips_button()

    @unittest.skip("pass")
    def test_click_my_addresses_button(self):
        self.my_account.click_my_addresses_button()

    @unittest.skip("pass")
    def test_click_my_personal_information_button(self):
        self.my_account.click_my_personal_information_button()


if __name__ == '__main__':
    unittest.main()
