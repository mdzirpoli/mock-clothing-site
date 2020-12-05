"""
Created on November 29, 2020

@author: Mark Zirpoli

This module contains all page web element types
"""
from selenium import webdriver


class Element(object):
    """
    Element main class
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        self.driver = driver
        self.div_id = div_id
        self.xpath = xpath
        self.div_name = div_name
        self._element = None

    @property
    def element(self):
        if self.div_id:
            return self.driver.find_element_by_id(self.div_id)
        elif self.xpath:
            return self.driver.find_element_by_xpath(self.xpath)
        elif self.div_name:
            return self.driver.find_element_by_name(self.div_name)


class Button(Element):
    """
    Class that implements a button object
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        super().__init__(driver, div_id, xpath, div_name)

    def click(self):
        try:
            self.element.click()
        except Exception as e:
            print(e)


class Link(Element):
    """
    Class that implements a link object
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        super().__init__(driver, div_id, xpath, div_name)

    def click(self):
        try:
            self.element.click()
        except Exception as e:
            print(e)


class DropDown(Element):
    """
    Class that implements a dropdown object
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        super().__init__(driver, div_id, xpath, div_name)

    def select_dropdown(self, dropdown: str):
        try:
            self.element.send_keys(dropdown)
        except Exception as e:
            print(e)


class TextField(Element):
    """
    Class that implements a textfield object
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        super().__init__(driver, div_id, xpath, div_name)

    def input_text(self, text: str):
        try:
            self.element.send_keys(text)
        except Exception as e:
            print(e)


class CheckBox(Element):
    """
    Class that implements a checkbox object
    """
    def __init__(self, driver: webdriver, div_id=None, xpath=None,
                 div_name=None):
        super().__init__(driver, div_id, xpath, div_name)

    def check(self):
        if self.element:
            try:
                if not self.element.is_selected():
                    self.element.click()
            except Exception as e:
                print(e)

    def uncheck(self):
        if self.element:
            try:
                if self.element.is_selected():
                    self.element.click()
            except Exception as e:
                print(e)
