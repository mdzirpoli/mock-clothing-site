"""
Created on November 16, 2019

@author: Mark Zirpoli

This module contains the unit tests for the Sign In page
"""

from Pages.SignInPage import SignInPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class SignInPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.click_sign_in_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_create_account_email_address_textbox(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.input_create_account_email_address_textbox("joesmith@email.com")

    @unittest.skip("pass")
    def test_click_create_an_account_button(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.click_create_an_account_button()

    @unittest.skip("pass")
    def test_input_email_address_textbox(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.input_email_address_textbox("email@email.com")

    @unittest.skip("pass")
    def test_input_password_textbox(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.input_password_textbox("abcd1234")

    @unittest.skip("pass")
    def test_click_sign_in_button(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.click_sign_in_button()

    @unittest.skip("pass")
    def test_forgot_your_password_link(self):
        driver = self.driver
        sign_in = SignInPage(driver)
        sign_in.click_forgot_your_password_link()


if __name__ == '__main__':
    unittest.main()
