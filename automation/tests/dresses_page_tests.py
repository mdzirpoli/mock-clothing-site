"""
Created on January 20, 2020
Modified on December 27, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Dresses page
"""

from automation.pages.dresses_page import DressesPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class DressesPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.dresses = DressesPage(self.driver)
        self.dresses.click_dresses_nav_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_dresses_casual_dresses_link(self):
        self.dresses.click_dresses_casual_dresses_link()

    @unittest.skip("pass")
    def test_click_dresses_evening_dresses_link(self):
        self.dresses.click_dresses_evening_dresses_link()

    @unittest.skip("pass")
    def test_click_dresses_summer_dresses_link(self):
        self.dresses.click_dresses_summer_dresses_link()

    @unittest.skip("pass")
    def test_check_categories_casual_dresses_checkbox(self):
        self.dresses.check_categories_casual_dresses_checkbox()

    @unittest.skip("pass")
    def test_uncheck_categories_casual_dresses_checkbox(self):
        self.dresses.uncheck_categories_casual_dresses_checkbox()

    @unittest.skip("pass")
    def test_check_categories_evening_dresses_checkbox(self):
        self.dresses.check_categories_evening_dresses_checkbox()

    @unittest.skip("pass")
    def test_uncheck_categories_evening_dresses_checkbox(self):
        self.dresses.uncheck_categories_evening_dresses_checkbox()

    @unittest.skip("pass")
    def test_check_categories_summer_dresses_checkbox(self):
        self.dresses.check_categories_summer_dresses_checkbox()

    @unittest.skip("pass")
    def test_uncheck_categories_summer_dresses_checkbox(self):
        self.dresses.uncheck_categories_summer_dresses_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_size_small_checkbox(self):
        self.dresses.check_dresses_size_small_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_size_small_checkbox(self):
        self.dresses.uncheck_dresses_size_small_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_size_medium_checkbox(self):
        self.dresses.check_dresses_size_medium_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_size_medium_checkbox(self):
        self.dresses.uncheck_dresses_size_medium_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_size_large_checkbox(self):
        self.dresses.check_dresses_size_large_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_size_large_checkbox(self):
        self.dresses.uncheck_dresses_size_large_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_beige_checkbox(self):
        self.dresses.check_dresses_color_beige_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_beige_checkbox(self):
        self.dresses.uncheck_dresses_color_beige_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_white_checkbox(self):
        self.dresses.check_dresses_color_white_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_white_checkbox(self):
        self.dresses.uncheck_dresses_color_white_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_black_checkbox(self):
        self.dresses.check_dresses_color_black_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_black_checkbox(self):
        self.dresses.uncheck_dresses_color_black_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_orange_checkbox(self):
        self.dresses.check_dresses_color_orange_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_orange_checkbox(self):
        self.dresses.uncheck_dresses_color_orange_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_blue_checkbox(self):
        self.dresses.check_dresses_color_blue_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_blue_checkbox(self):
        self.dresses.uncheck_dresses_color_blue_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_green_checkbox(self):
        self.dresses.check_dresses_color_green_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_green_checkbox(self):
        self.dresses.uncheck_dresses_color_green_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_yellow_checkbox(self):
        self.dresses.check_dresses_color_yellow_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_yellow_checkbox(self):
        self.dresses.uncheck_dresses_color_yellow_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_color_pink_checkbox(self):
        self.dresses.check_dresses_color_pink_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_color_pink_checkbox(self):
        self.dresses.uncheck_dresses_color_pink_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_compositions_cotton_checkbox(self):
        self.dresses.check_dresses_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_compositions_cotton_checkbox(self):
        self.dresses.uncheck_dresses_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_compositions_polyester_checkbox(self):
        self.dresses.check_dresses_compositions_polyester_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_compositions_polyester_checkbox(self):
        self.dresses.uncheck_dresses_compositions_polyester_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_compositions_viscose_checkbox(self):
        self.dresses.check_dresses_compositions_viscose_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_compositions_viscose_checkbox(self):
        self.dresses.uncheck_dresses_compositions_viscose_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_styles_casual_checkbox(self):
        self.dresses.check_dresses_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_styles_casual_checkbox(self):
        self.dresses.uncheck_dresses_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_styles_dressy_checkbox(self):
        self.dresses.check_dresses_styles_dressy_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_styles_dressy_checkbox(self):
        self.dresses.uncheck_dresses_styles_dressy_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_styles_girly_checkbox(self):
        self.dresses.check_dresses_styles_girly_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_styles_girly_checkbox(self):
        self.dresses.uncheck_dresses_styles_girly_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_properties_colorful_dress_checkbox(self):
        self.dresses.check_dresses_properties_colorful_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_properties_colorful_dress_checkbox(self):
        self.dresses.uncheck_dresses_properties_colorful_dress_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_properties_maxi_dress_checkbox(self):
        self.dresses.check_dresses_properties_maxi_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_properties_maxi_dress_checkbox(self):
        self.dresses.uncheck_dresses_properties_maxi_dress_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_properties_midi_dress_checkbox(self):
        self.dresses.check_dresses_properties_midi_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_properties_midi_dress_checkbox(self):
        self.dresses.uncheck_dresses_properties_midi_dress_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_properties_short_dress_checkbox(self):
        self.dresses.check_dresses_properties_short_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_properties_short_dress_checkbox(self):
        self.dresses.uncheck_dresses_properties_short_dress_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_availability_in_stock_checkbox(self):
        self.dresses.check_dresses_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_availability_in_stock_checkbox(self):
        self.dresses.uncheck_dresses_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_manufacturer_fashion_manufacturer_checkbox(self):
        self.dresses.check_dresses_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_manufacturer_fashion_manufacturer_checkbox(self):
        self.dresses.uncheck_dresses_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_check_dresses_condition_new_checkbox(self):
        self.dresses.check_dresses_condition_new_checkbox()

    @unittest.skip("pass")
    def test_uncheck_dresses_condition_new_checkbox(self):
        self.dresses.uncheck_dresses_condition_new_checkbox()

    @unittest.skip("pass")
    def test_click_dresses_information_delivery_link(self):
        self.dresses.click_dresses_information_delivery_link()

    @unittest.skip("pass")
    def test_click_dresses_information_legal_notice_link(self):
        self.dresses.click_dresses_information_legal_notice_link()

    @unittest.skip("pass")
    def test_click_dresses_information_terms_and_conditions_of_use_link(self):
        self.dresses.click_dresses_information_terms_and_conditions_of_use_link()

    @unittest.skip("pass")
    def test_click_dresses_information_about_us_link(self):
        self.dresses.click_dresses_information_about_us_link()

    @unittest.skip("pass")
    def test_click_dresses_information_secure_payment_link(self):
        self.dresses.click_dresses_information_secure_payment_link()

    @unittest.skip("pass")
    def test_click_dresses_information_our_stores_link(self):
        self.dresses.click_dresses_information_our_stores_link()

    @unittest.skip("pass")
    def test_click_dresses_all_specials_button(self):
        self.dresses.click_dresses_all_specials_button()

    @unittest.skip("pass")
    def test_click_dresses_discover_our_stores_button(self):
        self.dresses.click_dresses_discover_our_stores_button()

    @unittest.skip("pass")
    def test_select_subcategories_casual_dresses_thumbnail(self):
        self.dresses.click_subcategories_casual_dresses_thumbnail()

    @unittest.skip("pass")
    def test_select_subcategories_evening_dresses_thumbnail(self):
        self.dresses.click_subcategories_evening_dresses_thumbnail()

    @unittest.skip("pass")
    def test_select_subcategories_summer_dresses_thumbnail(self):
        self.dresses.click_subcategories_summer_dresses_thumbnail()

    @unittest.skip("pass")
    def test_select_dresses_sort_by_dropdown(self):
        self.dresses.select_dresses_sort_by_dropdown("In stock")

    @unittest.skip("pass")
    def test_click_dresses_view_grid_button(self):
        self.dresses.click_dresses_view_grid_button()

    @unittest.skip("pass")
    def test_click_dresses_list_grid_button(self):
        self.dresses.click_dresses_list_grid_button()

    @unittest.skip("pass")
    def test_click_printed_chiffon_dress_thumbnail(self):
        self.dresses.click_printed_chiffon_dress_thumbnail()

    @unittest.skip("pass")
    def test_click_printed_chiffon_dress_quick_view_button(self):
        self.dresses.click_printed_chiffon_dress_quick_view_button()


if __name__ == '__main__':
    unittest.main()
