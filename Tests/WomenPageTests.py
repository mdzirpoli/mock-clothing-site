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


if __name__ == '__main__':
    unittest.main()
