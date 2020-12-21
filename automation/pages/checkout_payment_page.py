"""
Created on March 14, 2020
Modified on December 21, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Payment page
"""

from automation.elements import Button, Link


class CheckoutPaymentPage(object):
    """
    Page object for Checkout Payment page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_checkout_payment_pay_by_bank_wire_button(self):
        checkout_payment_pay_by_bank_wire = \
            Button(self.driver,
                   xpath="//*[contains(text(), 'Pay by bank wire')]")
        checkout_payment_pay_by_bank_wire.click()

    def click_checkout_payment_pay_by_check_button(self):
        checkout_payment_pay_by_check = \
            Button(self.driver,
                   xpath="//*[contains(text(), 'Pay by check')]")
        checkout_payment_pay_by_check.click()

    def click_checkout_payment_continue_shopping_link(self):
        checkout_payment_continue_shopping = \
            Link(self.driver, xpath="//*[@title='Previous']")
        checkout_payment_continue_shopping.click()
