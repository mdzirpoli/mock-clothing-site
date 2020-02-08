"""
Created on February 8, 2020

@author: Mark Zirpoli

This module contains methods for the Search Box
"""

from selenium.webdriver.common.by import By


class SearchBox(object):
    """
    Page object for Search Box
    """

    # Search box locators
    SEARCH_US_TEXTBOX = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")

    def __init__(self, driver):
        self.driver = driver

    def input_search_textbox(self, search):
        self.driver.find_element(*self.SEARCH_US_TEXTBOX).send_keys(search)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

