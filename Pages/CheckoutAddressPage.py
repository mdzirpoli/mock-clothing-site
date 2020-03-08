"""
Created on March 8, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Address page
"""
from selenium.webdriver.common.by import By


class CheckoutAddressPage(object):
    """
    Page object for Checkout Address page
    """

    # Checkout Address page locators
    CHECKOUT_ADDRESS_DELIVERY_ADDRESS_DROPDOWN = (By.ID, "id_address_delivery")
    CHECKOUT_ADDRESS_DELIVERY_ADDRESS_AS_BILLING_ADDRESS_CHECKBOX = (By.ID, "addressesAreEquals")
    CHECKOUT_ADDRESS_DELIVERY_ADDRESS_UPDATE_BUTTON = (By.XPATH, "//*[@id='address_delivery']/li[7]/a/span")
    CHECKOUT_ADDRESS_BILLING_ADDRESS_UPDATE_BUTTON = (By.XPATH, "//*[@id='address_invoice']/li[7]/a/span")
    CHECKOUT_ADDRESS_ADD_A_NEW_ADDRESS_BUTTON = (By.XPATH, "//*[@id='center_column']/form/div/p/a/span")
    CHECKOUT_ADDRESS_COMMENT_TO_ORDER_TEXTBOX = (By.NAME, "message")
    CHECKOUT_ADDRESS_CONTINUE_SHOPPING_LINK = (By.XPATH, "//*[@title='Previous']")
    CHECKOUT_ADDRESS_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='center_column']/form/p/button/span")

    def __init__(self, driver):
        self.driver = driver

    def select_choose_a_deliver_address_dropdown(self, email):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_DELIVERY_ADDRESS_DROPDOWN).send_keys(email)

    def click_delivery_address_as_billing_address(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_DELIVERY_ADDRESS_AS_BILLING_ADDRESS_CHECKBOX).click()

    def click_your_delivery_address_update_button(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_DELIVERY_ADDRESS_UPDATE_BUTTON).click()

    def click_your_billing_address_update_button(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_BILLING_ADDRESS_UPDATE_BUTTON).click()

    def click_add_a_new_address_button(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_ADD_A_NEW_ADDRESS_BUTTON).click()

    def input_comment_on_your_order_textbox(self, text):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_COMMENT_TO_ORDER_TEXTBOX).send_keys(text)

    def click_checkout_address_continue_shopping_link(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_CONTINUE_SHOPPING_LINK).click()

    def click_checkout_address_proceed_to_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_ADDRESS_PROCEED_TO_CHECKOUT_BUTTON).click()
