"""
Created on December 1, 2019

@author: Mark Zirpoli

This module contains methods for the Women page
"""

from Pages.BasePageObject import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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

    # Styles locators
    STYLES_CASUAL_CHECKBOX = (By.ID, "layered_id_feature_11")
    STYLES_DRESSY_CHECKBOX = (By.ID, "layered_id_feature_16")
    STYLES_GIRLY_CHECKBOX = (By.ID, "layered_id_feature_13")

    # Properties locators
    PROPERTIES_COLORFUL_DRESS_CHECKBOX = (By.ID, "layered_id_feature_18")
    PROPERTIES_MAXI_DRESS_CHECKBOX = (By.ID, "layered_id_feature_21")
    PROPERTIES_MIDI_DRESS_CHECKBOX = (By.ID, "layered_id_feature_20")
    PROPERTIES_SHORT_DRESS_CHECKBOX = (By.ID, "layered_id_feature_19")
    PROPERTIES_SHORT_SLEEVE_CHECKBOX = (By.ID, "layered_id_feature_17")

    # Availability locators
    AVAILABILITY_IN_STOCK_CHECKBOX = (By.ID, "layered_quantity_1")

    # Manufacturer locators
    MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX = (By.ID, "layered_manufacturer_1")

    # Condition locators
    CONDITION_NEW_CHECKBOX = (By.ID, "layered_condition_new")

    # Information locators
    INFORMATION_DELIVERY_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[1]/a")
    INFORMATION_LEGAL_NOTICE_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[2]/a")
    INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[3]/a")
    INFORMATION_ABOUT_US_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[4]/a")
    INFORMATION_SECURE_PAYMENT_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[5]/a")
    INFORMATION_OUR_STORES_LINK = (By.XPATH, "//*[@id='informations_block_left_1']/div/ul/li[6]/a")

    # Products locators
    SUBCATEGORIES_TOPS_THUMBNAIL = (By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/div[1]/a/img")
    SUBCATEGORIES_DRESSES_THUMBNAIL = (By.XPATH, "//*[@id='subcategories']/ul/li[2]/div[1]/a/img")
    SORT_BY_DROPDOWN = (By.ID, "selectProductSort")
    VIEW_GRID_BUTTON = (By.XPATH, "//*[@id='grid']/a/i")
    VIEW_LIST_BUTTON = (By.XPATH, "//*[@id='list']/a/i")

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

    def select_styles_casual_checkbox(self):
        self.driver.find_element(*WomenPage.STYLES_CASUAL_CHECKBOX).click()

    def select_styles_dressy_checkbox(self):
        self.driver.find_element(*WomenPage.STYLES_DRESSY_CHECKBOX).click()

    def select_styles_girly_checkbox(self):
        self.driver.find_element(*WomenPage.STYLES_GIRLY_CHECKBOX).click()

    def select_properties_colorful_dress_checkbox(self):
        self.driver.find_element(*WomenPage.PROPERTIES_COLORFUL_DRESS_CHECKBOX).click()

    def select_properties_maxi_dress_checkbox(self):
        self.driver.find_element(*WomenPage.PROPERTIES_MAXI_DRESS_CHECKBOX).click()

    def select_properties_midi_dress_checkbox(self):
        self.driver.find_element(*WomenPage.PROPERTIES_MIDI_DRESS_CHECKBOX).click()

    def select_properties_short_dress_checkbox(self):
        self.driver.find_element(*WomenPage.PROPERTIES_SHORT_DRESS_CHECKBOX).click()

    def select_properties_short_sleeve_checkbox(self):
        self.driver.find_element(*WomenPage.PROPERTIES_SHORT_SLEEVE_CHECKBOX).click()

    def select_availability_in_stock_checkbox(self):
        self.driver.find_element(*WomenPage.AVAILABILITY_IN_STOCK_CHECKBOX).click()

    def select_manufacturer_fashion_manufacturer_checkbox(self):
        self.driver.find_element(*WomenPage.MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX).click()

    def select_condition_new_checkbox(self):
        self.driver.find_element(*WomenPage.CONDITION_NEW_CHECKBOX).click()

    def click_information_delivery_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_DELIVERY_LINK).click()

    def click_information_legal_notice_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_LEGAL_NOTICE_LINK).click()

    def click_information_terms_and_conditions_of_use_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK).click()

    def click_information_about_us_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_ABOUT_US_LINK).click()

    def click_information_secure_payment_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_SECURE_PAYMENT_LINK).click()

    def click_information_our_stores_link(self):
        self.driver.find_element(*WomenPage.INFORMATION_OUR_STORES_LINK).click()

    def select_subcategories_tops_thumbnail(self):
        self.driver.find_element(*WomenPage.SUBCATEGORIES_TOPS_THUMBNAIL).click()

    def select_subcategories_dresses_thumbnail(self):
        self.driver.find_element(*WomenPage.SUBCATEGORIES_DRESSES_THUMBNAIL).click()

    def select_sort_by_dropdown(self, value):
        dropdown = Select(self.driver.find_element(*WomenPage.SORT_BY_DROPDOWN))
        dropdown.select_by_visible_text(value)

    def click_view_grid_button(self):
        self.driver.find_element(*WomenPage.VIEW_GRID_BUTTON).click()

    def click_list_grid_button(self):
        self.driver.find_element(*WomenPage.VIEW_LIST_BUTTON).click()


