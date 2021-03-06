"""
Created on December 1, 2019
Modified on December 21, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Women page
"""

from automation.pages.women_page import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class WomenPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_women_tops_link(self):
        self.women.click_women_tops_link()

    @unittest.skip("pass")
    def test_click_women_dresses_link(self):
        self.women.click_women_dresses_link()

    @unittest.skip("pass")
    def test_check_categories_tops_checkbox(self):
        self.women.check_categories_tops_checkbox()

    @unittest.skip("pass")
    def test_uncheck_categories_tops_checkbox(self):
        self.women.uncheck_categories_tops_checkbox()

    @unittest.skip("pass")
    def test_check_categories_dresses_checkbox(self):
        self.women.check_categories_dresses_checkbox()

    @unittest.skip("pass")
    def test_uncheck_categories_dresses_checkbox(self):
        self.women.uncheck_categories_dresses_checkbox()

    @unittest.skip("pass")
    def test_check_size_small_checkbox(self):
        self.women.check_size_small_checkbox()

    @unittest.skip("pass")
    def test_uncheck_size_small_checkbox(self):
        self.women.uncheck_size_small_checkbox()

    @unittest.skip("pass")
    def test_check_size_medium_checkbox(self):
        self.women.check_size_medium_checkbox()

    @unittest.skip("pass")
    def test_uncheck_size_medium_checkbox(self):
        self.women.uncheck_size_medium_checkbox()

    @unittest.skip("pass")
    def test_check_size_large_checkbox(self):
        self.women.check_size_large_checkbox()

    @unittest.skip("pass")
    def test_uncheck_size_large_checkbox(self):
        self.women.uncheck_size_large_checkbox()

    @unittest.skip("pass")
    def test_check_color_beige_checkbox(self):
        self.women.check_color_beige_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_beige_checkbox(self):
        self.women.uncheck_color_beige_checkbox()

    @unittest.skip("pass")
    def test_check_color_white_checkbox(self):
        self.women.check_color_white_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_white_checkbox(self):
        self.women.uncheck_color_white_checkbox()

    @unittest.skip("pass")
    def test_check_color_black_checkbox(self):
        self.women.check_color_black_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_black_checkbox(self):
        self.women.uncheck_color_black_checkbox()

    @unittest.skip("pass")
    def test_check_color_orange_checkbox(self):
        self.women.check_color_orange_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_orange_checkbox(self):
        self.women.uncheck_color_orange_checkbox()

    @unittest.skip("pass")
    def test_check_color_blue_checkbox(self):
        self.women.check_color_blue_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_blue_checkbox(self):
        self.women.uncheck_color_blue_checkbox()

    @unittest.skip("pass")
    def test_check_color_green_checkbox(self):
        self.women.check_color_green_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_green_checkbox(self):
        self.women.uncheck_color_green_checkbox()

    @unittest.skip("pass")
    def test_check_color_yellow_checkbox(self):
        self.women.check_color_yellow_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_yellow_checkbox(self):
        self.women.uncheck_color_yellow_checkbox()

    @unittest.skip("pass")
    def test_check_color_pink_checkbox(self):
        self.women.check_color_pink_checkbox()

    @unittest.skip("pass")
    def test_uncheck_color_pink_checkbox(self):
        self.women.uncheck_color_pink_checkbox()

    @unittest.skip("pass")
    def test_check_compositions_cotton_checkbox(self):
        self.women.check_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_uncheck_compositions_cotton_checkbox(self):
        self.women.uncheck_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_check_compositions_polyester_checkbox(self):
        self.women.check_compositions_polyester_checkbox()

    @unittest.skip("pass")
    def test_uncheck_compositions_polyester_checkbox(self):
        self.women.uncheck_compositions_polyester_checkbox()

    @unittest.skip("pass")
    def test_check_compositions_viscose_checkbox(self):
        self.women.check_compositions_viscose_checkbox()

    @unittest.skip("pass")
    def test_uncheck_compositions_viscose_checkbox(self):
        self.women.uncheck_compositions_viscose_checkbox()

    @unittest.skip("pass")
    def test_check_styles_casual_checkbox(self):
        self.women.check_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_uncheck_styles_casual_checkbox(self):
        self.women.uncheck_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_check_styles_dressy_checkbox(self):
        self.women.check_styles_dressy_checkbox()

    @unittest.skip("pass")
    def test_uncheck_styles_dressy_checkbox(self):
        self.women.uncheck_styles_dressy_checkbox()

    @unittest.skip("pass")
    def test_check_styles_girly_checkbox(self):
        self.women.check_styles_girly_checkbox()

    @unittest.skip("pass")
    def test_uncheck_styles_girly_checkbox(self):
        self.women.uncheck_styles_girly_checkbox()

    @unittest.skip("pass")
    def test_check_properties_colorful_dress_checkbox(self):
        self.women.check_properties_colorful_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_properties_colorful_dress_checkbox(self):
        self.women.uncheck_properties_colorful_dress_checkbox()

    @unittest.skip("pass")
    def test_check_properties_maxi_dress_checkbox(self):
        self.women.check_properties_maxi_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_properties_maxi_dress_checkbox(self):
        self.women.uncheck_properties_maxi_dress_checkbox()

    @unittest.skip("pass")
    def test_check_properties_midi_dress_checkbox(self):
        self.women.check_properties_midi_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_properties_midi_dress_checkbox(self):
        self.women.uncheck_properties_midi_dress_checkbox()

    @unittest.skip("pass")
    def test_check_properties_short_dress_checkbox(self):
        self.women.check_properties_short_dress_checkbox()

    @unittest.skip("pass")
    def test_uncheck_properties_short_dress_checkbox(self):
        self.women.uncheck_properties_short_dress_checkbox()

    @unittest.skip("pass")
    def test_check_properties_short_sleeve_checkbox(self):
        self.women.check_properties_short_sleeve_checkbox()

    @unittest.skip("pass")
    def test_uncheck_properties_short_sleeve_checkbox(self):
        self.women.uncheck_properties_short_sleeve_checkbox()

    @unittest.skip("pass")
    def test_check_availability_in_stock_checkbox(self):
        self.women.check_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_uncheck_availability_in_stock_checkbox(self):
        self.women.uncheck_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_check_manufacturer_fashion_manufacturer_checkbox(self):
        self.women.check_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_uncheck_manufacturer_fashion_manufacturer_checkbox(self):
        self.women.uncheck_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_check_condition_new_checkbox(self):
        self.women.check_condition_new_checkbox()

    @unittest.skip("pass")
    def test_uncheck_condition_new_checkbox(self):
        self.women.uncheck_condition_new_checkbox()

    @unittest.skip("pass")
    def test_click_information_legal_notice_link(self):
        self.women.click_information_legal_notice_link()

    @unittest.skip("pass")
    def test_click_information_terms_and_conditions_of_use_link(self):
        self.women.click_information_terms_and_conditions_of_use_link()

    @unittest.skip("pass")
    def test_click_information_about_us_link(self):
        self.women.click_information_about_us_link()

    @unittest.skip("pass")
    def test_click_information_secure_payment_link(self):
        self.women.click_information_secure_payment_link()

    @unittest.skip('pass')
    def test_click_information_our_stores_link(self):
        self.women.click_information_our_stores_link()

    @unittest.skip("pass")
    def test_click_women_all_specials_button(self):
        self.women.click_women_all_specials_button()

    @unittest.skip("pass")
    def test_click_women_discover_our_stores_button(self):
        self.women.click_women_discover_our_stores_button()

    @unittest.skip("pass")
    def test_select_subcategories_tops_thumbnail(self):
        self.women.select_subcategories_tops_thumbnail()

    @unittest.skip("pass")
    def test_select_subcategories_dresses_thumbnail(self):
        self.women.select_subcategories_dresses_thumbnail()

    @unittest.skip("pass")
    def test_select_sort_by_dropdown(self):
        self.women.select_sort_by_dropdown("In stock")

    @unittest.skip("pass")
    def test_click_view_grid_button(self):
        self.women.click_view_grid_button()

    @unittest.skip("pass")
    def test_click_list_grid_button(self):
        self.women.click_list_grid_button()

    @unittest.skip("pass")
    def test_click_blouse_thumbnail(self):
        self.women.click_blouse_thumbnail()

    @unittest.skip("pass")
    def test_click_blouse_hover_quick_view_button(self):
        self.women.click_blouse_hover_quick_view_button()

    @unittest.skip("pass")
    def test_click_blouse_hover_add_to_cart_button(self):
        self.women.click_blouse_hover_add_to_cart_button()

    @unittest.skip("pass")
    def test_click_blouse_hover_more_button(self):
        self.women.click_blouse_hover_more_button()

    @unittest.skip("pass")
    def test_click_blouse_hover_add_to_wishlist_button(self):
        self.women.click_blouse_hover_add_to_wishlist_button()

    @unittest.skip("pass")
    def test_click_blouse_hover_add_to_compare_button(self):
        self.women.click_blouse_hover_add_to_compare_button()


if __name__ == '__main__':
    unittest.main()
