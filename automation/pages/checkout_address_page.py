"""
Created on March 8, 2020
Modified on December 5, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Address page
"""

from automation.elements import Button, Link, DropDown, CheckBox, TextField


class CheckoutAddressPage(object):
    """
    Page object for Checkout Address page
    """
    def __init__(self, driver):
        self.driver = driver

    def select_choose_a_deliver_address_dropdown(self, address: str):
        choose_deliver_address_dropdown = \
            DropDown(self.driver, div_id="id_address_delivery")
        choose_deliver_address_dropdown.select_dropdown(address)

    def check_delivery_address_as_billing_checkbox(self):
        delivery_address_as_billing = CheckBox(self.driver,
                                               div_id="addressesAreEquals")
        delivery_address_as_billing.check()

    def uncheck_delivery_address_as_billing_checkbox(self):
        delivery_address_as_billing = CheckBox(self.driver,
                                               div_id="addressesAreEquals")
        delivery_address_as_billing.uncheck()

    def click_your_delivery_address_update_button(self):
        your_deliver_address_update = \
            Button(self.driver,
                   xpath="//*[@id='address_delivery']/li[7]/a/span")
        your_deliver_address_update.click()

    def click_your_billing_address_update_button(self):
        your_billing_address_update = \
            Button(self.driver,
                   xpath="//*[@id='address_invoice']/li[7]/a/span")
        your_billing_address_update.click()

    def click_add_a_new_address_button(self):
        add_new_address = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/form/div/p/a/span")
        add_new_address.click()

    def input_comment_on_your_order_textbox(self, text: str):
        comment_on_your_order = TextField(self.driver, div_name="message")
        comment_on_your_order.input_text(text)

    def click_checkout_address_continue_shopping_link(self):
        checkout_address_continue_shopping = \
            Link(self.driver, xpath="//*[@title='Previous']")
        checkout_address_continue_shopping.click()

    def click_checkout_address_proceed_to_checkout_button(self):
        checkout_address_proceed_to_checkout = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/form/p/button/span")
        checkout_address_proceed_to_checkout.click()
