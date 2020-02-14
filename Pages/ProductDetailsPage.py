"""
Created on November 8, 2020

@author: Mark Zirpoli

This module contains methods for the Women Blouse Product Details page
"""

from selenium.webdriver.common.by import By


class ProductDetailsPage(object):
    """
    Page object for the Women Blouse Product Details page
    """

    # Product page locators
    PRODUCT_DETAILS_PAGE_TWEET_BUTTON = (By.XPATH, "//*[@id='center_column']/div/div/div[3]/p[7]/button[1]")
    PRODUCT_DETAILS_PAGE_FACEBOOK_BUTTON = (By.XPATH, "//*[@id='center_column']/div/div/div[3]/p[7]/button[2]")
    PRODUCT_DETAILS_PAGE_GOOGLE_PLUS_BUTTON = (By.XPATH, "//*[@id='center_column']/div/div/div[3]/p[7]/button[3]")
    PRODUCT_DETAILS_PAGE_PINTEREST_BUTTON = (By.XPATH, "//*[@id='center_column']/div/div/div[3]/p[7]/button[4]")
    SEND_TO_A_FRIEND_LINK = (By.ID, "send_friend_button")
    PRINT_LINK = (By.XPATH, "//*[@id='usefull_link_block']/li[2]/a")
    QUANTITY_TEXTBOX = (By.ID, "quantity_wanted")
    QUANTITY_MINUS_BUTTON = (By.XPATH, "//*[@id='quantity_wanted_p']/a[1]/span/i")
    QUANTITY_PLUS_BUTTON = (By.XPATH, "//*[@id='quantity_wanted_p']/a[2]/span/i")
    PRODUCT_DETAILS_SIZE_DROPDOWN = (By.ID, "group_1")
    PRODUCT_DETAILS_PAGE_COLOR_WHITE_BUTTON = (By.ID, "color_8")
    PRODUCT_DETAILS_PAGE_COLOR_BLACK_BUTTON = (By.ID, "color_11")
    PRODUCT_DETAILS_PAGE_ADD_TO_CART_BUTTON = (By.NAME, "Submit")
    PRODUCT_DETAILS_PAGE_ADD_TO_WISHLIST_BUTTON = (By.ID, "wishlist_button")

    def __init__(self, driver):
        self.driver = driver

    def click_product_details_page_tweet_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_TWEET_BUTTON).click()

    def click_product_details_page_facebook_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_FACEBOOK_BUTTON).click()

    def click_product_details_page_google_plus_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_GOOGLE_PLUS_BUTTON).click()

    def click_product_details_page_pinterest_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_PINTEREST_BUTTON).click()

    def click_send_to_a_friend_link(self):
        self.driver.find_element(*self.SEND_TO_A_FRIEND_LINK).click()

    def click_product_details_page_print_link(self):
        self.driver.find_element(*self.PRINT_LINK).click()

    def input_quantity_textbox(self, quantity):
        self.driver.find_element(*self.QUANTITY_TEXTBOX).clear()
        self.driver.find_element(*self.QUANTITY_TEXTBOX).send_keys(quantity)

    def click_quantity_minus_button(self):
        self.driver.find_element(*self.QUANTITY_MINUS_BUTTON).click()

    def click_quantity_plus_button(self):
        self.driver.find_element(*self.QUANTITY_PLUS_BUTTON).click()

    def select_product_details_page_size_dropdown(self, size):
        self.driver.find_element(*self.PRODUCT_DETAILS_SIZE_DROPDOWN).send_keys(size)

    def click_product_details_page_color_white_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_COLOR_WHITE_BUTTON).click()

    def click_product_details_page_color_black_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_COLOR_BLACK_BUTTON).click()

    def click_product_details_page_add_to_cart_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_ADD_TO_CART_BUTTON).click()

    def click_product_details_page_add_to_wishlist_button(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_PAGE_ADD_TO_WISHLIST_BUTTON).click()

