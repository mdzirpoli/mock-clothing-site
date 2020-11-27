"""
Created on April 4, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Order History And Details page
"""

from pages.my_account_page import MyAccountPage
from pages.sign_in_page import SignInPage
from pages.order_history_and_details_page import OrderHistoryAndDetailsPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class OrderHistoryAndDetailsPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sign_in = SignInPage(self.driver)
        self.sign_in.click_sign_in_menu_button()
        self.sign_in.input_email_address_textbox("test1940@gmail.com")
        self.sign_in.input_password_textbox("abcd1234")
        self.sign_in.click_sign_in_button()
        self.my_account = MyAccountPage(self.driver)
        self.my_account.click_order_history_and_details_button()
        self.order_history = OrderHistoryAndDetailsPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_order_history_order_reference_link(self):
        self.order_history.click_order_history_order_reference_link()

    @unittest.skip("pass")
    def test_click_order_history_order_reference_reorder_button(self):
        self.order_history.click_order_history_order_reference_link()
        time.sleep(2)
        self.order_history.click_order_history_order_reference_reorder_button()

    @unittest.skip("pass")
    def test_click_order_history_order_reference_download_your_invoice_as_pdf(self):
        self.order_history.click_order_history_order_reference_link()
        time.sleep(2)
        self.order_history.click_order_history_order_reference_download_your_invoice_as_pdf()

    @unittest.skip("pass")
    def test_select_order_history_order_reference_product_message_dropdown(self):
        self.order_history.click_order_history_order_reference_link()
        time.sleep(2)
        self.order_history.select_order_history_order_reference_product_message_dropdown("Blouse - Color : Black, Size : S")

    @unittest.skip("pass")
    def test_input_order_history_order_reference_product_message_textbox(self):
        self.order_history.click_order_history_order_reference_link()
        time.sleep(2)
        self.order_history.input_order_history_order_reference_product_message_textbox("Product text for this field")

    @unittest.skip("pass")
    def test_click_order_history_order_reference_product_message_send_button(self):
        self.order_history.click_order_history_order_reference_link()
        time.sleep(2)
        self.order_history.click_order_history_order_reference_product_message_send_button()

    @unittest.skip("pass")
    def test_click_order_history_invoice_pdf_link(self):
        self.order_history.click_order_history_invoice_pdf_link()

    @unittest.skip("pass")
    def test_click_order_history_details_button(self):
        self.order_history.click_order_history_details_button()

    @unittest.skip("pass")
    def test_click_order_history_reorder_link(self):
        self.order_history.click_order_history_reorder_link()

    @unittest.skip("pass")
    def test_click_order_history_back_to_your_account_button(self):
        self.order_history.click_order_history_back_to_your_account_button()

    @unittest.skip("pass")
    def test_click_order_history_home_button(self):
        self.order_history.click_order_history_home_button()


if __name__ == '__main__':
    unittest.main()
