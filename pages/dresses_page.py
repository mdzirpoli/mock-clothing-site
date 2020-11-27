"""
Created on January 20, 2020

@author: Mark Zirpoli

This module contains methods for the Dresses page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class DressesPage(object):
    """
    Page object for Dresses page
    """

    # Dresses page navigation menu locator
    DRESSES_NAV_MENU_BUTTON = (By.XPATH, "//*[@id='block_top_menu']/ul/li[2]/a")

    # Dresses Casual, Evening and Summer Dresses locators
    DRESSES_CASUAL_DRESSES_LINK = (By.XPATH, "//*[@id='categories_block_left']/div/ul/li[1]/a")
    DRESSES_EVENING_DRESSES_LINK = (By.XPATH, "//*[@id='categories_block_left']/div/ul/li[2]/a")
    DRESSES_SUMMER_DRESSES_LINK = (By.XPATH, "//*[@id='categories_block_left']/div/ul/li[3]/a")

    # Categories locators
    CATEGORIES_CASUAL_DRESSES_CHECKBOX = (By.ID, "layered_category_9")
    CATEGORIES_EVENING_DRESSES_CHECKBOX = (By.ID, "layered_category_10")
    CATEGORIES_SUMMER_DRESSES_CHECKBOX = (By.ID, "layered_category_11")

    # Size locators
    DRESSES_SIZE_SMALL_CHECKBOX = (By.ID, "layered_id_attribute_group_1")
    DRESSES_SIZE_MEDIUM_CHECKBOX = (By.ID, "layered_id_attribute_group_2")
    DRESSES_SIZE_LARGE_CHECKBOX = (By.ID, "layered_id_attribute_group_3")

    # Color locators
    DRESSES_COLOR_BEIGE_CHECKBOX = (By.ID, "layered_id_attribute_group_7")
    DRESSES_COLOR_WHITE_CHECKBOX = (By.ID, "layered_id_attribute_group_8")
    DRESSES_COLOR_BLACK_CHECKBOX = (By.ID, "layered_id_attribute_group_11")
    DRESSES_COLOR_ORANGE_CHECKBOX = (By.ID, "layered_id_attribute_group_13")
    DRESSES_COLOR_BLUE_CHECKBOX = (By.ID, "layered_id_attribute_group_14")
    DRESSES_COLOR_GREEN_CHECKBOX = (By.ID, "layered_id_attribute_group_15")
    DRESSES_COLOR_YELLOW_CHECKBOX = (By.ID, "layered_id_attribute_group_16")
    DRESSES_COLOR_PINK_CHECKBOX = (By.ID, "layered_id_attribute_group_24")

    # Compositions locators
    DRESSES_COMPOSITIONS_COTTON_CHECKBOX = (By.ID, "layered_id_feature_5")
    DRESSES_COMPOSITIONS_POLYESTER_CHECKBOX = (By.ID, "layered_id_feature_1")
    DRESSES_COMPOSITIONS_VISCOSE_CHECKBOX = (By.ID, "layered_id_feature_3")

    # Styles locators
    DRESSES_STYLES_CASUAL_CHECKBOX = (By.ID, "layered_id_feature_11")
    DRESSES_STYLES_DRESSY_CHECKBOX = (By.ID, "layered_id_feature_16")
    DRESSES_STYLES_GIRLY_CHECKBOX = (By.ID, "layered_id_feature_13")

    # Properties locators
    DRESSES_PROPERTIES_COLORFUL_DRESS_CHECKBOX = (By.ID, "layered_id_feature_18")
    DRESSES_PROPERTIES_MAXI_DRESS_CHECKBOX = (By.ID, "layered_id_feature_21")
    DRESSES_PROPERTIES_MIDI_DRESS_CHECKBOX = (By.ID, "layered_id_feature_20")
    DRESSES_PROPERTIES_SHORT_DRESS_CHECKBOX = (By.ID, "layered_id_feature_19")

    # Availability locators
    DRESSES_AVAILABILITY_IN_STOCK_CHECKBOX = (By.ID, "layered_quantity_1")

    # Manufacturer locators
    DRESSES_MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX = (By.ID, "layered_manufacturer_1")

    # Condition locators
    DRESSES_CONDITION_NEW_CHECKBOX = (By.ID, "layered_condition_new")

    # Information locators
    DRESSES_INFORMATION_DELIVERY_LINK = (By.XPATH, "//*[@title='Delivery']")
    DRESSES_INFORMATION_LEGAL_NOTICE_LINK = (By.XPATH, "//*[@title='Legal Notice']")
    DRESSES_INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK = (By.XPATH, "//*[@title='Terms and conditions of use']")
    DRESSES_INFORMATION_ABOUT_US_LINK = (By.XPATH, "//*[@title='About us']")
    DRESSES_INFORMATION_SECURE_PAYMENT_LINK = (By.XPATH, "//*[@title='Secure payment']")
    DRESSES_INFORMATION_OUR_STORES_LINK = (By.XPATH, "//*[@title='Our stores']")

    # Specials
    DRESSES_ALL_SPECIALS_BUTTON = (By.XPATH, "//span[text()='All specials']")

    # Our Stores
    DRESSES_DISCOVER_OUR_STORES_BUTTON = (By.XPATH, "//span[text()='Discover our stores']")

    # Products locators
    SUBCATEGORIES_CASUAL_DRESSES_THUMBNAIL = (By.XPATH, "//*[@id='subcategories']/ul/li[1]/div[1]/a/img")
    SUBCATEGORIES_EVENING_DRESSES_THUMBNAIL = (By.XPATH, "//*[@id='subcategories']/ul/li[2]/div[1]/a/img")
    SUBCATEGORIES_SUMMER_DRESSES_THUMBNAIL = (By.XPATH, "//*[@id='subcategories']/ul/li[3]/div[1]/a/img")
    DRESSES_SORT_BY_DROPDOWN = (By.ID, "selectProductSort")
    DRESSES_VIEW_GRID_BUTTON = (By.XPATH, "//*[@id='grid']/a/i")
    DRESSES_VIEW_LIST_BUTTON = (By.XPATH, "//*[@id='list']/a/i")

    # Printed Chiffon Dress locators
    PRINTED_CHIFFON_DRESS_THUMBNAIL = (By.XPATH, "//*[@title='Printed Chiffon Dress'][1]")
    PRINTED_CHIFFON_DRESS_QUICK_VIEW_BUTTON = (By.XPATH, "//span[text()='Quick view']")
    PRINTED_CHIFFON_DRESS_ADD_TO_CART_BUTTON = (By.XPATH, "//span[text()='Add to cart']")
    PRINTED_CHIFFON_DRESS_MORE_BUTTON = (By.XPATH, "//span[text()='More']")

    def __init__(self, driver):
        self.driver = driver

    def click_dresses_nav_menu_button(self):
        self.driver.find_element(*self.DRESSES_NAV_MENU_BUTTON).click()

    def click_dresses_casual_dresses_link(self):
        self.driver.find_element(*self.DRESSES_CASUAL_DRESSES_LINK).click()

    def click_dresses_evening_dresses_link(self):
        self.driver.find_element(*self.DRESSES_EVENING_DRESSES_LINK).click()

    def click_dresses_summer_dresses_link(self):
        self.driver.find_element(*self.DRESSES_SUMMER_DRESSES_LINK).click()

    def select_categories_casual_dresses_checkbox(self):
        self.driver.find_element(*self.CATEGORIES_CASUAL_DRESSES_CHECKBOX).click()

    def select_categories_evening_dresses_checkbox(self):
        self.driver.find_element(*self.CATEGORIES_EVENING_DRESSES_CHECKBOX).click()

    def select_categories_summer_dresses_checkbox(self):
        self.driver.find_element(*self.CATEGORIES_SUMMER_DRESSES_CHECKBOX).click()

    def select_dresses_size_small_checkbox(self):
        self.driver.find_element(*self.DRESSES_SIZE_SMALL_CHECKBOX).click()

    def select_dresses_size_medium_checkbox(self):
        self.driver.find_element(*self.DRESSES_SIZE_MEDIUM_CHECKBOX).click()

    def select_dresses_size_large_checkbox(self):
        self.driver.find_element(*self.DRESSES_SIZE_LARGE_CHECKBOX).click()

    def select_dresses_color_beige_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_BEIGE_CHECKBOX).click()

    def select_dresses_color_white_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_WHITE_CHECKBOX).click()

    def select_dresses_color_black_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_BLACK_CHECKBOX).click()

    def select_dresses_color_orange_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_ORANGE_CHECKBOX).click()

    def select_dresses_color_blue_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_BLUE_CHECKBOX).click()

    def select_dresses_color_green_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_GREEN_CHECKBOX).click()

    def select_dresses_color_yellow_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_YELLOW_CHECKBOX).click()

    def select_dresses_color_pink_checkbox(self):
        self.driver.find_element(*self.DRESSES_COLOR_PINK_CHECKBOX).click()

    def select_dresses_compositions_cotton_checkbox(self):
        self.driver.find_element(*self.DRESSES_COMPOSITIONS_COTTON_CHECKBOX).click()

    def select_dresses_compositions_polyester_checkbox(self):
        self.driver.find_element(*self.DRESSES_COMPOSITIONS_POLYESTER_CHECKBOX).click()

    def select_dresses_compositions_viscose_checkbox(self):
        self.driver.find_element(*self.DRESSES_COMPOSITIONS_VISCOSE_CHECKBOX).click()

    def select_dresses_styles_casual_checkbox(self):
        self.driver.find_element(*self.DRESSES_STYLES_CASUAL_CHECKBOX).click()

    def select_dresses_styles_dressy_checkbox(self):
        self.driver.find_element(*self.DRESSES_STYLES_DRESSY_CHECKBOX).click()

    def select_dresses_styles_girly_checkbox(self):
        self.driver.find_element(*self.DRESSES_STYLES_GIRLY_CHECKBOX).click()

    def select_dresses_properties_colorful_dress_checkbox(self):
        self.driver.find_element(*self.DRESSES_PROPERTIES_COLORFUL_DRESS_CHECKBOX).click()

    def select_dresses_properties_maxi_dress_checkbox(self):
        self.driver.find_element(*self.DRESSES_PROPERTIES_MAXI_DRESS_CHECKBOX).click()

    def select_dresses_properties_midi_dress_checkbox(self):
        self.driver.find_element(*self.DRESSES_PROPERTIES_MIDI_DRESS_CHECKBOX).click()

    def select_dresses_properties_short_dress_checkbox(self):
        self.driver.find_element(*self.DRESSES_PROPERTIES_SHORT_DRESS_CHECKBOX).click()

    def select_dresses_availability_in_stock_checkbox(self):
        self.driver.find_element(*self.DRESSES_AVAILABILITY_IN_STOCK_CHECKBOX).click()

    def select_dresses_manufacturer_fashion_manufacturer_checkbox(self):
        self.driver.find_element(*self.DRESSES_MANUFACTURER_FASHION_MANUFACTURER_CHECKBOX).click()

    def select_dresses_condition_new_checkbox(self):
        self.driver.find_element(*self.DRESSES_CONDITION_NEW_CHECKBOX).click()

    def click_dresses_information_delivery_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_DELIVERY_LINK).click()

    def click_dresses_information_legal_notice_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_LEGAL_NOTICE_LINK).click()

    def click_dresses_information_terms_and_conditions_of_use_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK).click()

    def click_dresses_information_about_us_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_ABOUT_US_LINK).click()

    def click_dresses_information_secure_payment_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_SECURE_PAYMENT_LINK).click()

    def click_dresses_information_our_stores_link(self):
        self.driver.find_element(*self.DRESSES_INFORMATION_OUR_STORES_LINK).click()

    def click_dresses_all_specials_button(self):
        self.driver.find_element(*self.DRESSES_ALL_SPECIALS_BUTTON).click()

    def click_dresses_discover_our_stores_button(self):
        self.driver.find_element(*self.DRESSES_DISCOVER_OUR_STORES_BUTTON).click()

    def select_subcategories_casual_dresses_thumbnail(self):
        self.driver.find_element(*self.SUBCATEGORIES_CASUAL_DRESSES_THUMBNAIL).click()

    def select_subcategories_evening_dresses_thumbnail(self):
        self.driver.find_element(*self.SUBCATEGORIES_EVENING_DRESSES_THUMBNAIL).click()

    def select_subcategories_summer_dresses_thumbnail(self):
        self.driver.find_element(*self.SUBCATEGORIES_SUMMER_DRESSES_THUMBNAIL).click()

    def select_dresses_sort_by_dropdown(self, value):
        dropdown = Select(self.driver.find_element(*self.DRESSES_SORT_BY_DROPDOWN))
        dropdown.select_by_visible_text(value)

    def click_dresses_view_grid_button(self):
        self.driver.find_element(*self.DRESSES_VIEW_GRID_BUTTON).click()

    def click_dresses_list_grid_button(self):
        self.driver.find_element(*self.DRESSES_VIEW_LIST_BUTTON).click()

    def click_printed_chiffon_dress_thumbnail(self):
        self.driver.find_element(*self.PRINTED_CHIFFON_DRESS_THUMBNAIL).click()

    def click_printed_chiffon_dress_quick_view_button(self):
        button = self.driver.find_element(*self.PRINTED_CHIFFON_DRESS_QUICK_VIEW_BUTTON)
        thumbnail = self.driver.find_element(*self.PRINTED_CHIFFON_DRESS_THUMBNAIL)
        hover = ActionChains(self.driver).move_to_element(button).move_to_element(thumbnail)
        hover.click().perform()
