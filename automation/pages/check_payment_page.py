"""
Created on May 30, 2020

@author: Mark Zirpoli

This module contains methods for the Check Payment page
"""
from selenium.webdriver.common.by import By


class CheckPaymentPage(object):
    """
    Page object for Check Payment page
    """

    # Check Payment page locators
    CHECK_PAYMENT_OTHER_PAYMENT_METHODS_LINK = (By.XPATH, "// *[ @ id = 'cart_navigation'] / a")
    CHECK_PAYMENT_I_CONFIRM_MY_ORDER_BUTTON = (By.XPATH, "//*[contains(text(), 'I confirm my order')]")

    def __init__(self, driver):
        self.driver = driver

    def click_check_payment_other_payment_methods_link(self):
        self.driver.find_element(*self.CHECK_PAYMENT_OTHER_PAYMENT_METHODS_LINK).click()

    def click_check_payment_i_confirm_my_order_button(self):
        self.driver.find_element(*self.CHECK_PAYMENT_I_CONFIRM_MY_ORDER_BUTTON).click()

    def verify_check_payment_text(self, text):
        try:
            self.driver.find_element_by_xpath("//*[contains(text(),'" + text + "')]")
        except Exception:
            raise Exception(f"The text cannot be found")
