"""
Created on January 26, 2020

@author: Mark Zirpoli

This module contains methods for the T-Shirts page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class TShirtsPage(object):
    """
    Page object for T-Shirts page
    """

    # T-shirts page navigation menu locator
    TSHIRTS_NAV_MENU_BUTTON = (By.XPATH, "//*[@id='block_top_menu']/ul/li[3]/a")

    # Size locators
    TSHIRTS_SIZE_SMALL_CHECKBOX = (By.ID, "layered_id_attribute_group_1")
    TSHIRTS_SIZE_MEDIUM_CHECKBOX = (By.ID, "layered_id_attribute_group_2")
    TSHIRTS_SIZE_LARGE_CHECKBOX = (By.ID, "layered_id_attribute_group_3")

    # Color locators
    TSHIRTS_COLOR_ORANGE_CHECKBOX = (By.ID, "layered_id_attribute_group_13")
    TSHIRTS_COLOR_BLUE_CHECKBOX = (By.ID, "layered_id_attribute_group_14")

    # Compositions locators
    TSHIRTS_COMPOSITIONS_COTTON_CHECKBOX = (By.ID, "layered_id_feature_5")

    # Styles locators
    TSHIRTS_STYLES_CASUAL_CHECKBOX = (By.ID, "layered_id_feature_11")

    # Properties locators
    TSHIRTS_PROPERTIES_SHORT_SLEEVE_CHECKBOX = (By.ID, "layered_id_feature_17")

    # Availability locators
    TSHIRTS_AVAILABILITY_IN_STOCK_CHECKBOX = (By.ID, "layered_quantity_1")

    # Manufacturer locators
    TSHIRTS_MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX = (By.ID, "layered_manufacturer_1")

    # Condition locators
    TSHIRTS_CONDITION_NEW_CHECKBOX = (By.ID, "layered_condition_new")

    # Information locators
    TSHIRTS_INFORMATION_DELIVERY_LINK = (By.XPATH, "//*[@title='Delivery']")
    TSHIRTS_INFORMATION_LEGAL_NOTICE_LINK = (By.XPATH, "//*[@title='Legal Notice']")
    TSHIRTS_INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK = (By.XPATH, "//*[@title='Terms and conditions of use']")
    TSHIRTS_INFORMATION_ABOUT_US_LINK = (By.XPATH, "//*[@title='About us']")
    TSHIRTS_INFORMATION_SECURE_PAYMENT_LINK = (By.XPATH, "//*[@title='Secure payment']")
    TSHIRTS_INFORMATION_OUR_STORES_LINK = (By.XPATH, "//*[@title='Our stores']")

    # Specials
    TSHIRTS_ALL_SPECIALS_BUTTON = (By.XPATH, "//span[text()='All specials']")

    # Our Stores
    TSHIRTS_DISCOVER_OUR_STORES_BUTTON = (By.XPATH, "//span[text()='Discover our stores']")

    # Products locators
    TSHIRTS_SORT_BY_DROPDOWN = (By.ID, "selectProductSort")
    TSHIRTS_VIEW_GRID_BUTTON = (By.XPATH, "//*[@id='grid']/a/i")
    TSHIRTS_VIEW_LIST_BUTTON = (By.XPATH, "//*[@id='list']/a/i")

    # Faded Short Sleeve T-Shirt locators
    FADED_SHORT_SLEEVE_TSHIRT_THUMBNAIL = (By.XPATH, "//*[@title='Faded Short Sleeve T-shirts'][1]")
    FADED_SHORT_SLEEVE_TSHIRT_QUICK_VIEW_BUTTON = (By.XPATH, "//span[text()='Quick view']")
    FADED_SHORT_SLEEVE_TSHIRT_ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")
    FADED_SHORT_SLEEVE_TSHIRT_MORE_BUTTON = (By.XPATH, "//span[text()='More']")

    def __init__(self, driver):
        self.driver = driver

    def click_tshirts_nav_menu_button(self):
        self.driver.find_element(*self.TSHIRTS_NAV_MENU_BUTTON).click()

    def click_tshirts_size_small_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_SIZE_SMALL_CHECKBOX).click()

    def click_tshirts_size_medium_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_SIZE_MEDIUM_CHECKBOX).click()

    def click_tshirts_size_large_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_SIZE_LARGE_CHECKBOX).click()

    def click_tshirts_color_orange_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_COLOR_ORANGE_CHECKBOX).click()

    def click_tshirts_color_blue_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_COLOR_BLUE_CHECKBOX).click()

    def click_tshirts_compositions_cotton_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_COMPOSITIONS_COTTON_CHECKBOX).click()

    def click_tshirts_styles_casual_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_STYLES_CASUAL_CHECKBOX).click()

    def click_tshirts_properties_short_sleeve_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_PROPERTIES_SHORT_SLEEVE_CHECKBOX).click()

    def click_tshirts_availability_in_stock_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_AVAILABILITY_IN_STOCK_CHECKBOX).click()

    def click_tshirts_manufacturer_fashion_manufacturer_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX).click()

    def click_tshirts_condition_new_checkbox(self):
        self.driver.find_element(*self.TSHIRTS_CONDITION_NEW_CHECKBOX).click()

    def click_tshirts_information_delivery_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_DELIVERY_LINK).click()

    def click_tshirts_legal_notice_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_LEGAL_NOTICE_LINK).click()

    def click_tshirts_terms_and_condition_of_use_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK).click()

    def click_tshirts_about_us_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_ABOUT_US_LINK).click()

    def click_tshirts_secure_payment_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_SECURE_PAYMENT_LINK).click()

    def click_tshirts_our_stores_link(self):
        self.driver.find_element(*self.TSHIRTS_INFORMATION_OUR_STORES_LINK).click()

    def click_tshirts_all_specials_button(self):
        self.driver.find_element(*self.TSHIRTS_ALL_SPECIALS_BUTTON).click()

    def click_tshirts_discover_our_stores_button(self):
        self.driver.find_element(*self.TSHIRTS_DISCOVER_OUR_STORES_BUTTON).click()

    def select_tshirts_sort_by_dropdown(self, value):
        dropdown = Select(self.driver.find_element(*self.TSHIRTS_SORT_BY_DROPDOWN))
        dropdown.select_by_visible_text(value)

    def click_tshirts_view_grid_button(self):
        self.driver.find_element(*self.TSHIRTS_VIEW_GRID_BUTTON).click()

    def click_tshirts_list_grid_button(self):
        self.driver.find_element(*self.TSHIRTS_VIEW_LIST_BUTTON).click()

    def click_faded_short_sleeve_tshirts_thumbnail(self):
        self.driver.find_element(*self.FADED_SHORT_SLEEVE_TSHIRT_THUMBNAIL).click()

    def click_printed_chiffon_dress_quick_view_button(self):
        button = self.driver.find_element(*self.FADED_SHORT_SLEEVE_TSHIRT_QUICK_VIEW_BUTTON)
        thumbnail = self.driver.find_element(*self.FADED_SHORT_SLEEVE_TSHIRT_THUMBNAIL)
        hover = ActionChains(self.driver).move_to_element(button).move_to_element(thumbnail)
        hover.click().perform()




