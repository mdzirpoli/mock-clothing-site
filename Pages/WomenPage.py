"""
Created on December 1, 2019

@author: Mark Zirpoli

This module contains methods for the Women page
"""

from Pages.BasePageObject import BasePage
from selenium.webdriver.common.by import By


class WomenPage(BasePage):
    """
    Page object for Women page
    """

    # Women page navigation menu locator
    WOMEN_NAV_MENU_BUTTON = (By.XPATH, "//*[@id='block_top_menu']/ul/li[1]/a")

    # Categories locators
    CATEGORIES_TOPS_CHECKBOX = (By.ID, "layered_category_4")
    CATEGORIES_DRESSES_CHECKBOX = (By.ID, "layered_category_8")

    # Size locators
    SIZE_SMALL_CHECKBOX = (By.ID, "layered_id_attribute_group_1")
    SIZE_MEDIUM_CHECKBOX = (By.ID, "layered_id_attribute_group_2")
    SIZE_LARGE_CHECKBOX = (By.ID, "layered_id_attribute_group_3")

    # Color locators
    COLOR_BEIGE_CHECKBOX = (By.ID, "layered_id_attribute_group_7")
    COLOR_WHITE_CHECKBOX = (By.ID, "layered_id_attribute_group_8")
    COLOR_BLACK_CHECKBOX = (By.ID, "layered_id_attribute_group_11")
    COLOR_ORANGE_CHECKBOX = (By.ID, "layered_id_attribute_group_13")
    COLOR_BLUE_CHECKBOX = (By.ID, "layered_id_attribute_group_14")
    COLOR_GREEN_CHECKBOX = (By.ID, "layered_id_attribute_group_15")
    COLOR_YELLOW_CHECKBOX = (By.ID, "layered_id_attribute_group_16")
    COLOR_PINK_CHECKBOX = (By.ID, "layered_id_attribute_group_24")

    # Compositions locators
    COMPOSITIONS_COTTON_CHECKBOX = (By.ID, "layered_id_feature_5")
    COMPOSITIONS_POLYESTER_CHECKBOX = (By.ID, "layered_id_feature_1")
    COMPOSITIONS_VISCOSE_CHECKBOX = (By.ID, "layered_id_feature_3")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_women_nav_menu_button(self):
        self.driver.find_element(*WomenPage.WOMEN_NAV_MENU_BUTTON).click()

    def select_categories_tops_checkbox(self):
        self.driver.find_element(*WomenPage.CATEGORIES_TOPS_CHECKBOX).click()

    def select_categories_dresses_checkbox(self):
        self.driver.find_element(*WomenPage.CATEGORIES_DRESSES_CHECKBOX).click()

    def select_size_small_checkbox(self):
        self.driver.find_element(*WomenPage.SIZE_SMALL_CHECKBOX).click()

    def select_size_medium_checkbox(self):
        self.driver.find_element(*WomenPage.SIZE_MEDIUM_CHECKBOX).click()

    def select_size_large_checkbox(self):
        self.driver.find_element(*WomenPage.SIZE_LARGE_CHECKBOX).click()

    def select_color_beige_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_BEIGE_CHECKBOX).click()

    def select_color_white_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_WHITE_CHECKBOX).click()

    def select_color_black_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_BLACK_CHECKBOX).click()

    def select_color_orange_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_ORANGE_CHECKBOX).click()

    def select_color_blue_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_BLUE_CHECKBOX).click()

    def select_color_green_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_GREEN_CHECKBOX).click()

    def select_color_yellow_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_YELLOW_CHECKBOX).click()

    def select_color_pink_checkbox(self):
        self.driver.find_element(*WomenPage.COLOR_PINK_CHECKBOX).click()

    def select_compositions_cotton_checkbox(self):
        self.driver.find_element(*WomenPage.COMPOSITIONS_COTTON_CHECKBOX).click()

    def select_compositions_polyester_checkbox(self):
        self.driver.find_element(*WomenPage.COMPOSITIONS_POLYESTER_CHECKBOX).click()

    def select_compositions_viscose_checkbox(self):
        self.driver.find_element(*WomenPage.COMPOSITIONS_VISCOSE_CHECKBOX).click()
