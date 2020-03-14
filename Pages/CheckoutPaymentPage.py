"""
Created on March 14, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Payment page
"""
from selenium.webdriver.common.by import By


class CheckoutPaymentPage(object):
    """
    Page object for Checkout Payment page
    """

    # Checkout Payment page locators
    CHECKOUT_PAYMENT_PAY_BY_BANK_WIRE_BUTTON = (By.XPATH, "//*[contains(text(), 'Pay by bank wire')]")
    CHECKOUT_PAYMENT_PAY_BY_CHECK_BUTTON = (By.XPATH, "//*[contains(text(), 'Pay by check')]")
    CHECKOUT_PAYMENT_CONTINUE_SHOPPING_LINK = (By.XPATH, "//*[@title='Previous']")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_payment_pay_by_bank_wire_button(self):
        self.driver.find_element(*self.CHECKOUT_PAYMENT_PAY_BY_BANK_WIRE_BUTTON).click()

    def click_checkout_payment_pay_by_check_button(self):
        self.driver.find_element(*self.CHECKOUT_PAYMENT_PAY_BY_CHECK_BUTTON).click()

    def click_checkout_payment_continue_shopping_link(self):
        self.driver.find_element(*self.CHECKOUT_PAYMENT_CONTINUE_SHOPPING_LINK).click()
