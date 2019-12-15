"""
Created on December 1, 2019

@author: Mark Zirpoli

This module contains the unit tests for the Women page
"""

from Pages.WomenPage import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class WomenPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        driver = self.driver
        women = WomenPage(driver)
        women.click_women_nav_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_select_categories_tops_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_categories_tops_checkbox()

    @unittest.skip("pass")
    def test_select_categories_dresses_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_categories_dresses_checkbox()

    @unittest.skip("pass")
    def test_select_size_small_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_size_small_checkbox()

    @unittest.skip("pass")
    def test_select_size_medium_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_size_medium_checkbox()

    @unittest.skip("pass")
    def test_select_size_large_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_size_large_checkbox()

    @unittest.skip("pass")
    def test_select_color_beige_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_beige_checkbox()

    @unittest.skip("pass")
    def test_select_color_white_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_white_checkbox()

    @unittest.skip("pass")
    def test_select_color_black_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_black_checkbox()

    @unittest.skip("pass")
    def test_select_color_orange_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_orange_checkbox()

    @unittest.skip("pass")
    def test_select_color_blue_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_blue_checkbox()

    @unittest.skip("pass")
    def test_select_color_green_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_green_checkbox()

    @unittest.skip("pass")
    def test_select_color_yellow_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_yellow_checkbox()

    @unittest.skip("pass")
    def test_select_color_pink_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_color_pink_checkbox()

    @unittest.skip("pass")
    def test_select_compositions_cotton_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_compositions_cotton_checkbox()

    @unittest.skip("pass")
    def test_select_compositions_polyester_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_compositions_polyester_checkbox()

    @unittest.skip("pass")
    def test_select_compositions_viscose_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_compositions_viscose_checkbox()

    @unittest.skip("pass")
    def test_select_styles_casual_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_styles_casual_checkbox()

    @unittest.skip("pass")
    def test_select_styles_dressy_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_styles_dressy_checkbox()

    @unittest.skip("pass")
    def test_select_styles_girly_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_styles_girly_checkbox()

    @unittest.skip("pass")
    def test_select_properties_colorful_dress_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_properties_colorful_dress_checkbox()

    @unittest.skip("pass")
    def test_select_properties_maxi_dress_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_properties_maxi_dress_checkbox()

    @unittest.skip("pass")
    def test_select_properties_midi_dress_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_properties_midi_dress_checkbox()

    @unittest.skip("pass")
    def test_select_properties_short_dress_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_properties_short_dress_checkbox()

    @unittest.skip("pass")
    def test_select_properties_short_sleeve_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_properties_short_sleeve_checkbox()

    @unittest.skip("pass")
    def test_select_availability_in_stock_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_availability_in_stock_checkbox()

    @unittest.skip("pass")
    def test_select_manufacturer_fashion_manufacturer_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_manufacturer_fashion_manufacturer_checkbox()

    @unittest.skip("pass")
    def test_select_condition_new_checkbox(self):
        driver = self.driver
        women = WomenPage(driver)
        women.select_condition_new_checkbox()


if __name__ == '__main__':
    unittest.main()
