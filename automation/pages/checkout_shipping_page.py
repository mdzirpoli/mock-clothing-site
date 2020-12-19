"""
Created on March 14, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Shipping page
"""

from automation.elements import Button, Link, CheckBox


class CheckoutShippingPage(object):
    """
    Page object for Checkout Shipping page
    """
    def __init__(self, driver):
        self.driver = driver

    def check_checkout_shipping_terms_of_service_checkbox(self):
        checkout_shipping_terms_of_service = CheckBox(self.driver,
                                                      div_id="cgv")
        checkout_shipping_terms_of_service.check()

    def uncheck_checkout_shipping_terms_of_service_checkbox(self):
        checkout_shipping_terms_of_service = CheckBox(self.driver,
                                                      div_id="cgv")
        checkout_shipping_terms_of_service.uncheck()

    def click_checkout_shipping_read_the_terms_of_service_link(self):
        checkout_shipping_read_the_terms_of_service = \
            Link(self.driver,
                 xpath="//*[contains(text(), 'Read the Terms of Service')]")
        checkout_shipping_read_the_terms_of_service.click()

    def click_checkout_shipping_continue_shopping_link(self):
        checkout_shipping_continue_shopping = \
            Link(self.driver, xpath="//*[@title='Previous']")
        checkout_shipping_continue_shopping.click()

    def click_checkout_shipping_proceed_to_checkout_button(self):
        checkout_shipping_proceed_to_checkout = \
            Button(self.driver, xpath="//*[@id='form']/p/button/span")
        checkout_shipping_proceed_to_checkout.click()
