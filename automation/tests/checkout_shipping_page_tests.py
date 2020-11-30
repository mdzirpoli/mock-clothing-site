"""
Created on March 14, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Checkout Shipping page
"""

from automation.pages.product_details_page import ProductDetailsPage
from automation.pages.components.modals.add_to_cart_modal import AddToCartModal
from automation.pages.checkout_summary_page import CheckoutSummaryPage
from automation.pages.checkout_address_page import CheckoutAddressPage
from automation.pages.checkout_shipping_page import CheckoutShippingPage
from automation.pages.sign_in_page import SignInPage
from automation.pages.women_page import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class CheckoutShippingPageTests(unittest.TestCase):

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
        self.address.click_checkout_address_proceed_to_checkout_button()
        self.shipping = CheckoutShippingPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_checkout_shipping_terms_of_service_checkbox(self):
        time.sleep(2)
        self.shipping.click_checkout_shipping_terms_of_service_checkbox()

    @unittest.skip("pass")
    def test_click_checkout_shipping_read_the_terms_of_service(self):
        time.sleep(2)
        self.shipping.click_checkout_shipping_read_the_terms_of_service_link()

    @unittest.skip("pass")
    def test_click_checkout_shipping_continue_shopping_link(self):
        time.sleep(2)
        self.shipping.click_checkout_shipping_continue_shopping_link()

    @unittest.skip("pass")
    def test_click_checkout_shipping_proceed_to_checkout_button(self):
        time.sleep(2)
        self.shipping.click_checkout_shipping_proceed_to_checkout_button()


if __name__ == '__main__':
    unittest.main()
