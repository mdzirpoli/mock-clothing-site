"""
Created on March 8, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Checkout Address page
"""

from automation.pages.product_details_page import ProductDetailsPage
from automation.pages.components.modals.add_to_cart_modal import AddToCartModal
from automation.pages.checkout_summary_page import CheckoutSummaryPage
from automation.pages.checkout_address_page import CheckoutAddressPage
from automation.pages.sign_in_page import SignInPage
from automation.pages.women_page import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class CheckoutAddressPageTests(unittest.TestCase):

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
        self.summary.click_checkout_summary_proceed_to_checkout_button()
        self.address = CheckoutAddressPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_select_choose_a_deliver_address_dropdown(self):
        time.sleep(2)
        self.address.select_choose_a_deliver_address_dropdown("test@email.com")

    @unittest.skip("pass")
    def test_click_delivery_address_as_billing_address(self):
        time.sleep(2)
        self.address.click_delivery_address_as_billing_address()

    @unittest.skip("pass")
    def test_click_your_delivery_address_update_button(self):
        time.sleep(2)
        self.address.click_your_delivery_address_update_button()

    @unittest.skip("pass")
    def test_click_your_billing_address_update_button(self):
        time.sleep(2)
        self.address.click_your_billing_address_update_button()

    @unittest.skip("pass")
    def test_click_add_a_new_address_button(self):
        time.sleep(2)
        self.address.click_add_a_new_address_button()

    @unittest.skip("pass")
    def test_input_comment_on_your_order_textbox(self):
        time.sleep(2)
        self.address.input_comment_on_your_order_textbox("Comment about my order")

    @unittest.skip("pass")
    def test_click_checkout_address_continue_shopping_link(self):
        time.sleep(2)
        self.address.click_checkout_address_continue_shopping_link()

    @unittest.skip("pass")
    def test_click_checkout_address_proceed_to_checkout_button(self):
        time.sleep(2)
        self.address.click_checkout_address_proceed_to_checkout_button()


if __name__ == '__main__':
    unittest.main()
