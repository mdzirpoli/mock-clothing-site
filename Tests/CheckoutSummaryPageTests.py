"""
Created on February 29, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Checkout Summary page
"""

from Pages.ProductDetailsPage import ProductDetailsPage
from Pages.Components.Modals.AddToCartModal import AddToCartModal
from Pages.CheckoutSummaryPage import CheckoutSummaryPage
from Pages.SignInPage import SignInPage
from Pages.WomenPage import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class CheckoutSummaryPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sign_in = SignInPage(self.driver)
        self.sign_in.click_sign_in_menu_button()
        self.sign_in.input_email_address_textbox("test1940@gmail.com")
        self.sign_in.input_password_textbox("abcd1234")
        self.sign_in.click_sign_in_button()
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()
        self.women.click_blouse_thumbnail()
        self.product_details = ProductDetailsPage(self.driver)
        self.product_details.click_product_details_page_add_to_cart_button()
        time.sleep(2)
        self.cart_modal = AddToCartModal(self.driver)
        self.cart_modal.click_add_to_cart_modal_proceed_to_checkout_button()
        self.summary = CheckoutSummaryPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_checkout_summary_quantity_textbox(self):
        time.sleep(2)
        self.summary.input_checkout_summary_quantity_textbox("3")

    @unittest.skip("pass")
    def test_click_checkout_summary_minus_button(self):
        time.sleep(2)
        self.summary.click_checkout_summary_minus_button()

    @unittest.skip("pass")
    def test_click_checkout_summary_plus_button(self):
        time.sleep(2)
        self.summary.click_checkout_summary_plus_button()

    @unittest.skip("pass")
    def test_click_checkout_summary_trashcan_button(self):
        time.sleep(2)
        self.summary.click_checkout_summary_trashcan_button()

    @unittest.skip("pass")
    def test_click_checkout_summary_proceed_to_checkout_button(self):
        time.sleep(2)
        self.summary.click_checkout_summary_proceed_to_checkout_button()

    @unittest.skip("pass")
    def test_click_checkout_summary_continue_shopping_link(self):
        time.sleep(2)
        self.summary.click_checkout_summary_continue_shopping_link()


if __name__ == '__main__':
    unittest.main()
