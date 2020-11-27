"""
Created on February 8, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Search Box
"""

from pages.components.search_box import SearchBox
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class SearchBoxTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.search = SearchBox(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_search_textbox(self):
        self.search.input_search_textbox("pants")

    @unittest.skip("pass")
    def test_click_search_button(self):
        self.search.click_search_button()


if __name__ == '__main__':
    unittest.main()
