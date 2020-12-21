"""
Created on February 4, 2020
Modified on December 21, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Create An Account page
"""

from automation.pages.create_account_page import CreateAnAccountPage
from automation.pages.sign_in_page import SignInPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class CreateAnAccountPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sign_in = SignInPage(self.driver)
        self.sign_in.click_sign_in_menu_button()
        self.sign_in.input_create_account_email_address_textbox("email494549@email.com")
        self.sign_in.click_create_an_account_button()
        self.account = CreateAnAccountPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_select_title_mr_radio_button(self):
        time.sleep(2)
        self.account.select_title_mr_radio_button()

    @unittest.skip("pass")
    def test_select_title_mrs_radio_button(self):
        time.sleep(2)
        self.account.select_title_mrs_radio_button()

    @unittest.skip("pass")
    def test_input_your_personal_information_first_name_textbox(self):
        time.sleep(2)
        self.account.input_your_personal_information_first_name_textbox("John")

    @unittest.skip("pass")
    def test_input_your_personal_information_last_name_textbox(self):
        time.sleep(2)
        self.account.input_your_personal_information_last_name_textbox("Smith")

    @unittest.skip("pass")
    def test_input_your_personal_information_email_textbox(self):
        time.sleep(2)
        self.account.input_your_personal_information_email_textbox("email@email.com")

    @unittest.skip("pass")
    def test_input_your_personal_information_password_textbox(self):
        time.sleep(2)
        self.account.input_your_personal_information_password_textbox("abcd1234")

    @unittest.skip("pass")
    def test_select_date_of_birth_days_dropdown(self):
        time.sleep(2)
        self.account.select_date_of_birth_days_dropdown("9")

    @unittest.skip("pass")
    def test_select_date_of_birth_month_dropdown(self):
        time.sleep(2)
        self.account.select_date_of_birth_month_dropdown("January")

    @unittest.skip("pass")
    def test_select_date_of_birth_year_dropdown(self):
        time.sleep(2)
        self.account.select_date_of_birth_year_dropdown("1985")

    @unittest.skip("pass")
    def test_check_newsletter_checkbox(self):
        time.sleep(2)
        self.account.check_newsletter_checkbox()

    @unittest.skip("pass")
    def test_uncheck_newsletter_checkbox(self):
        time.sleep(2)
        self.account.uncheck_newsletter_checkbox()

    @unittest.skip("pass")
    def test_check_special_offers_checkbox(self):
        time.sleep(2)
        self.account.check_special_offers_checkbox()

    @unittest.skip("pass")
    def test_uncheck_special_offers_checkbox(self):
        time.sleep(2)
        self.account.uncheck_special_offers_checkbox()

    @unittest.skip("pass")
    def test_input_your_address_first_name_textbox(self):
        time.sleep(2)
        self.account.input_your_address_first_name_textbox("Joe")

    @unittest.skip("pass")
    def test_input_your_address_last_name_textbox(self):
        time.sleep(2)
        self.account.input_your_address_last_name_textbox("Smith")

    @unittest.skip("pass")
    def test_input_your_address_company_textbox(self):
        time.sleep(2)
        self.account.input_your_address_company_textbox("Fake Company")

    @unittest.skip("pass")
    def test_input_your_address_address_textbox(self):
        time.sleep(2)
        self.account.input_your_address_address_textbox("123 Fake Lane")

    @unittest.skip("pass")
    def test_input_your_address_line_two_textbox(self):
        time.sleep(2)
        self.account.input_your_address_line_two_textbox("B100")

    @unittest.skip("pass")
    def test_input_your_address_city_textbox(self):
        time.sleep(2)
        self.account.input_your_address_city_textbox("Flagstaff")

    @unittest.skip("pass")
    def test_select_your_address_state_dropdown(self):
        time.sleep(2)
        self.account.select_your_address_state_dropdown("Arizona")

    @unittest.skip("pass")
    def test_input_your_address_zip_postal_code_textbox(self):
        time.sleep(2)
        self.account.input_your_address_zip_postal_code_textbox("86001")

    @unittest.skip("pass")
    def test_select_your_address_country_dropdown(self):
        time.sleep(2)
        self.account.select_your_address_country_dropdown("United States")

    @unittest.skip("pass")
    def test_input_your_address_additional_information_textbox(self):
        time.sleep(2)
        self.account.input_your_address_additional_information_textbox("Additional Information")

    @unittest.skip("pass")
    def test_input_your_address_home_phone_textbox(self):
        time.sleep(2)
        self.account.input_your_address_home_phone_textbox("555-555-8888")

    @unittest.skip("pass")
    def test_input_your_address_mobile_phone_textbox(self):
        time.sleep(2)
        self.account.input_your_address_mobile_phone_textbox("555-555-7777")

    @unittest.skip("pass")
    def test_input_your_address_alias_textbox(self):
        time.sleep(2)
        self.account.input_your_address_alias_textbox("Alias")

    @unittest.skip("pass")
    def test_click_your_address_register_button(self):
        time.sleep(2)
        self.account.click_your_address_register_button()


if __name__ == '__main__':
    unittest.main()
