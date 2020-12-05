"""
Created on May 30, 2020
Modified on December 5, 2020

@author: Mark Zirpoli

This module contains methods for the Check Payment page
"""
from automation.elements import Button, Link


class CheckPaymentPage(object):
    """
    Page object for Check Payment page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_check_payment_other_payment_methods_link(self):
        check_payment_other_payment_methods = \
            Link(self.driver, xpath="// *[ @ id = 'cart_navigation'] / a")
        check_payment_other_payment_methods.click()

    def click_check_payment_i_confirm_my_order_button(self):
        check_payment_confirm_my_order = \
            Button(self.driver,
                   xpath="//*[contains(text(), 'I confirm my order')]")
        check_payment_confirm_my_order.click()

    def verify_check_payment_text(self, text: str):
        try:
            self.driver.find_element_by_xpath("//*[contains(text(),'"
                                              + text + "')]")
        except Exception:
            raise Exception(f'{"The text cannot be found"}')
