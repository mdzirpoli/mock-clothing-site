"""
Created on February 29, 2020

@author: Mark Zirpoli

This module contains methods for the Add To Cart modal
"""

from selenium.webdriver.common.by import By


class AddToCartModal(object):
    """
    Page object for Add To Cart Modal
    """

    # Add To Cart Modal locators
    ADD_TO_CART_MODAL_CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[2]/div[4]/span/span")
    ADD_TO_CART_MODAL_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span")
    ADD_TO_CART_MODAL_X_BUTTON = (By.XPATH, "//*[@title='Close window']")

    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart_modal_continue_shopping_button(self):
        self.driver.find_element(*self.ADD_TO_CART_MODAL_CONTINUE_SHOPPING_BUTTON).click()

    def click_add_to_cart_modal_proceed_to_checkout_button(self):
        self.driver.find_element(*self.ADD_TO_CART_MODAL_PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_add_to_cart_modal_x_button(self):
        self.driver.find_element(*self.ADD_TO_CART_MODAL_X_BUTTON).click()