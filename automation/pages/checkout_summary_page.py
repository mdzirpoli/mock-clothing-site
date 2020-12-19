"""
Created on February 29, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Summary page
"""

from automation.elements import Button, TextField, Link


class CheckoutSummaryPage(object):
    """
    Page object for Checkout Summary page
    """
    def __init__(self, driver):
        self.driver = driver

    def input_checkout_summary_quantity_textbox(self, quantity):
        checkout_summary_quantity = \
            TextField(self.driver,
                      xpath="//*[@id='product_2_7_0_272223']/td[5]/input[2]")
        checkout_summary_quantity.input_text(quantity)

    def click_checkout_summary_minus_button(self):
        checkout_summary_minus = \
            Button(self.driver,
                   xpath="//*[@id='cart_quantity_down_2_7_0_272223']/span/i")
        checkout_summary_minus.click()

    def click_checkout_summary_plus_button(self):
        checkout_summary_plus = \
            Button(self.driver,
                   xpath="//*[@id='cart_quantity_up_2_7_0_272223']/span")
        checkout_summary_plus.click()

    def click_checkout_summary_trashcan_button(self):
        checkout_summary_trashcan = \
            Button(self.driver, xpath="//*[@id='2_7_0_272223']/i")
        checkout_summary_trashcan.click()

    def click_checkout_summary_proceed_to_checkout_button(self):
        checkout_summary_proceed_to_checkout = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/p[2]/a[1]/span")
        checkout_summary_proceed_to_checkout.click()

    def click_checkout_summary_continue_shopping_link(self):
        checkout_summary_continue_shopping = \
            Link(self.driver, xpath="//*[@id='center_column']/p[2]/a[2]")
        checkout_summary_continue_shopping.click()
