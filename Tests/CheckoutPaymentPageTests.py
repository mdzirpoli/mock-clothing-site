"""
Created on March 14, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Checkout Payment page
"""

from Pages.ProductDetailsPage import ProductDetailsPage
from Pages.Components.Modals.AddToCartModal import AddToCartModal
from Pages.CheckoutSummaryPage import CheckoutSummaryPage
from Pages.CheckoutAddressPage import CheckoutAddressPage
from Pages.CheckoutShippingPage import CheckoutShippingPage
from Pages.CheckoutPaymentPage import CheckoutPaymentPage
from Pages.SignInPage import SignInPage
from Pages.WomenPage import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class CheckoutPaymentPageTests(unittest.TestCase):

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
        self.shipping.click_checkout_shipping_terms_of_service_checkbox()
        self.shipping.click_checkout_shipping_proceed_to_checkout_button()
        self.payment = CheckoutPaymentPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_checkout_payment_pay_by_bank_wire_button(self):
        time.sleep(2)
        self.payment.click_checkout_payment_pay_by_bank_wire_button()

    @unittest.skip("pass")
    def test_click_checkout_payment_pay_by_check_button(self):
        time.sleep(2)
        self.payment.click_checkout_payment_pay_by_check_button()

    @unittest.skip("pass")
    def test_click_checkout_payment_continue_shopping_link(self):
        time.sleep(2)
        self.payment.click_checkout_payment_continue_shopping_link()


if __name__ == '__main__':
    unittest.main()