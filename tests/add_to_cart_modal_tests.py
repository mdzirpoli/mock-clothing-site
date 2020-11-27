"""
Created on February 29, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Add To Cart Modal
"""

from pages.product_details_page import ProductDetailsPage
from pages.women_page import WomenPage
from pages.components.modals.add_to_cart_modal import AddToCartModal
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class AddToCartModalTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()
        self.women.click_blouse_thumbnail()
        self.product_details = ProductDetailsPage(self.driver)
        self.product_details.click_product_details_page_add_to_cart_button()
        self.cart_modal = AddToCartModal(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_add_to_cart_modal_continue_shopping_button(self):
        time.sleep(2)
        self.cart_modal.click_add_to_cart_modal_continue_shopping_button()

    @unittest.skip("pass")
    def test_input_name_of_your_friend_textbox(self):
        time.sleep(2)
        self.cart_modal.click_add_to_cart_modal_proceed_to_checkout_button()

    @unittest.skip("pass")
    def test_click_add_to_cart_modal_x_button(self):
        time.sleep(2)
        self.cart_modal.click_add_to_cart_modal_x_button()


if __name__ == '__main__':
    unittest.main()
