"""
Created on January 26, 2020

@author: Mark Zirpoli

This module contains the unit tests for the T-Shirts page
"""

from Pages.TShirtsPage import TShirtsPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class TShirtPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.tshirts = TShirtsPage(self.driver)
        self.tshirts.click_tshirts_nav_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_tshirts_size_small_checkbox(self):
        self.tshirts.click_tshirts_size_small_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_size_medium_checkbox(self):
        self.tshirts.click_tshirts_size_medium_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_size_large_checkbox(self):
        self.tshirts.click_tshirts_size_large_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_color_orange_checkbox(self):
        self.tshirts.click_tshirts_color_orange_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_color_blue_checkbox(self):
        self.tshirts.click_tshirts_color_blue_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_compositions_cotton_checkbox(self):
        self.tshirts.click_tshirts_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_styles_casual_checkbox(self):
        self.tshirts.click_tshirts_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_properties_short_sleeve_checkbox(self):
        self.tshirts.click_tshirts_properties_short_sleeve_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_availability_in_stock_checkbox(self):
        self.tshirts.click_tshirts_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_manufacturer_fashion_manufacturer_checkbox(self):
        self.tshirts.click_tshirts_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_condition_new_checkbox(self):
        self.tshirts.click_tshirts_condition_new_checkbox()

    @unittest.skip("pass")
    def test_click_tshirts_information_delivery_link(self):
        self.tshirts.click_tshirts_information_delivery_link()

    @unittest.skip("pass")
    def test_click_tshirts_legal_notice_link(self):
        self.tshirts.click_tshirts_legal_notice_link()

    @unittest.skip("pass")
    def test_click_tshirts_terms_and_condition_of_use_link(self):
        self.tshirts.click_tshirts_terms_and_condition_of_use_link()

    @unittest.skip("pass")
    def test_click_tshirts_about_us_link(self):
        self.tshirts.click_tshirts_about_us_link()

    @unittest.skip("pass")
    def test_click_tshirts_secure_payment_link(self):
        self.tshirts.click_tshirts_secure_payment_link()

    @unittest.skip("pass")
    def test_click_tshirts_our_stores_link(self):
        self.tshirts.click_tshirts_our_stores_link()

    @unittest.skip("pass")
    def test_click_tshirts_all_specials_button(self):
        self.tshirts.click_tshirts_all_specials_button()

    @unittest.skip("pass")
    def test_click_tshirts_discover_our_stores_button(self):
        self.tshirts.click_tshirts_discover_our_stores_button()

    @unittest.skip("pass")
    def test_select_tshirts_sort_by_dropdown(self):
        self.tshirts.select_tshirts_sort_by_dropdown("In stock")

    @unittest.skip("pass")
    def test_click_tshirts_view_grid_button(self):
        self.tshirts.click_tshirts_view_grid_button()

    @unittest.skip("pass")
    def test_click_tshirts_list_grid_button(self):
        self.tshirts.click_tshirts_list_grid_button()

    @unittest.skip("pass")
    def test_click_faded_short_sleeve_tshirts_thumbnail(self):
        self.tshirts.click_faded_short_sleeve_tshirts_thumbnail()

    @unittest.skip("pass")
    def test_click_printed_chiffon_dress_quick_view_button(self):
        self.tshirts.click_printed_chiffon_dress_quick_view_button()


if __name__ == '__main__':
    unittest.main()
