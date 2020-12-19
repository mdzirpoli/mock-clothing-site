"""
Created on February 8, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Search Box
"""

from automation.elements import Button, TextField


class SearchBox(object):
    """
    Page object for Search Box
    """
    def __init__(self, driver):
        self.driver = driver

    def input_search_textbox(self, search):
        search_name = TextField(self.driver, div_id="search_query_top")
        search_name.input_text(search)

    def click_search_button(self):
        search_button = Button(self.driver, div_name="submit_search")
        search_button.click()
