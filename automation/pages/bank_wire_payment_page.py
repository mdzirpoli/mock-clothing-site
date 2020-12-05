"""
Created on April 12, 2020

@author: Mark Zirpoli

This module contains methods for the Bank Wire Payment page
"""
from automation.elements import Button, Link


class BankWirePaymentPage(object):
    """
    Page object for Bank Wire Payment page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_bank_wire_other_payment_methods_link(self):
        bank_wire_other_payment_methods = \
            Link(self.driver, xpath="// *[ @ id = 'cart_navigation'] / a")
        bank_wire_other_payment_methods.click()

    def click_bank_wire_i_confirm_my_order_button(self):
        bank_wire_confirm_my_order = \
            Button(self.driver,
                   xpath="//*[contains(text(), 'I confirm my order')]")
        bank_wire_confirm_my_order.click()

    def verify_bank_wire_text(self, text):
        try:
            self.driver.find_element_by_xpath("//*[contains(text(),'"
                                              + text + "')]")
        except Exception:
            raise Exception(f'{"The text cannot be found"}')
