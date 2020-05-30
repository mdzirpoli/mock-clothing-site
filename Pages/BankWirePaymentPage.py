"""
Created on April 12, 2020

@author: Mark Zirpoli

This module contains methods for the Bank Wire Payment page
"""
from selenium.webdriver.common.by import By


class BankWirePaymentPage(object):
    """
    Page object for Bank Wire Payment page
    """

    # Bank Wire Payment page locators
    BANK_WIRE_OTHER_PAYMENT_METHODS_LINK = (By.XPATH, "// *[ @ id = 'cart_navigation'] / a")
    BANK_WIRE_I_CONFIRM_MY_ORDER_BUTTON = (By.XPATH, "//*[contains(text(), 'I confirm my order')]")

    def __init__(self, driver):
        self.driver = driver

    def click_bank_wire_other_payment_methods_link(self):
        self.driver.find_element(*self.BANK_WIRE_OTHER_PAYMENT_METHODS_LINK).click()

    def click_bank_wire_i_confirm_my_order_button(self):
        self.driver.find_element(*self.BANK_WIRE_I_CONFIRM_MY_ORDER_BUTTON).click()

    def verify_bank_wire_text(self, text):
        try:
            self.driver.find_element_by_xpath("//*[contains(text(),'" + text + "')]")
        except Exception:
            raise Exception(f"The text cannot be found")
