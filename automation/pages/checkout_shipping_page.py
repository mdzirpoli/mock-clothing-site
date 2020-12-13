"""
Created on March 14, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Shipping page
"""

from selenium.webdriver.common.by import By


class CheckoutShippingPage(object):
    """
    Page object for Checkout Shipping page
    """

    # Checkout Shipping page locators
    CHECKOUT_SHIPPING_TERMS_OF_SERVICE_CHECKBOX = (By.ID, "cgv")
    CHECKOUT_SHIPPING_READ_THE_TERMS_OF_SERVICE_LINK = (By.XPATH, "//*[contains(text(), 'Read the Terms of Service')]")
    CHECKOUT_SHIPPING_CONTINUE_SHOPPING_LINK = (By.XPATH, "//*[@title='Previous']")
    CHECKOUT_SHIPPING_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='form']/p/button/span")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_shipping_terms_of_service_checkbox(self):
        self.driver.find_element(*self.CHECKOUT_SHIPPING_TERMS_OF_SERVICE_CHECKBOX).click()

    def click_checkout_shipping_read_the_terms_of_service_link(self):
        self.driver.find_element(*self.CHECKOUT_SHIPPING_READ_THE_TERMS_OF_SERVICE_LINK).click()

    def click_checkout_shipping_continue_shopping_link(self):
        self.driver.find_element(*self.CHECKOUT_SHIPPING_CONTINUE_SHOPPING_LINK).click()

    def click_checkout_shipping_proceed_to_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_SHIPPING_PROCEED_TO_CHECKOUT_BUTTON).click()
