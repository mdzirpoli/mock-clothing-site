"""
Created on February 8, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Women Blouse Product Details page
"""

from Pages.ProductDetailsPage import ProductDetailsPage
from Pages.WomenPage import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class ProductDetailsPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()
        self.women.click_blouse_thumbnail()
        self.product_details = ProductDetailsPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_product_details_page_tweet_button(self):
        self.product_details.click_product_details_page_tweet_button()

    @unittest.skip("pass")
    def test_click_product_details_page_facebook_button(self):
        self.product_details.click_product_details_page_facebook_button()

    @unittest.skip("pass")
    def test_click_product_details_page_google_plus_button(self):
        self.product_details.click_product_details_page_google_plus_button()

    @unittest.skip("pass")
    def test_click_product_details_page_pinterest_button(self):
        self.product_details.click_product_details_page_pinterest_button()

    @unittest.skip("pass")
    def test_click_send_to_a_friend_link(self):
        self.product_details.click_send_to_a_friend_link()

    @unittest.skip("pass")
    def test_click_product_details_page_print_link(self):
        self.product_details.click_product_details_page_print_link()

    @unittest.skip("pass")
    def test_input_quantity_textbox(self):
        self.product_details.input_quantity_textbox("3")

    @unittest.skip("pass")
    def test_click_quantity_minus_button(self):
        self.product_details.click_quantity_minus_button()

    @unittest.skip("pass")
    def test_click_quantity_plus_button(self):
        self.product_details.click_quantity_plus_button()

    @unittest.skip("pass")
    def test_select_product_details_page_size_dropdown(self):
        self.product_details.select_product_details_page_size_dropdown("M")

    @unittest.skip("pass")
    def test_click_product_details_page_color_white_button(self):
        self.product_details.click_product_details_page_color_white_button()

    @unittest.skip("pass")
    def test_click_product_details_page_color_black_button(self):
        self.product_details.click_product_details_page_color_black_button()

    @unittest.skip("pass")
    def test_click_product_details_page_add_to_cart_button(self):
        self.product_details.click_product_details_page_add_to_cart_button()

    @unittest.skip("pass")
    def test_click_product_details_page_add_to_wishlist_button(self):
        self.product_details.click_product_details_page_add_to_wishlist_button()


if __name__ == '__main__':
    unittest.main()
