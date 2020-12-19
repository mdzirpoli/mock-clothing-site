"""
Created on February 29, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Add To Cart modal
"""

from automation.elements import Button


class AddToCartModal(object):
    """
    Page object for Add To Cart Modal
    """
    def __init__(self, driver):
        self.driver = driver

    def click_add_to_cart_modal_continue_shopping_button(self):
        add_to_cart_modal_continue_shopping = \
            Button(self.driver,
                   xpath="//*[@id='layer_cart']/div[1]/div[2]/div[4]/span/span")
        add_to_cart_modal_continue_shopping.click()

    def click_add_to_cart_modal_proceed_to_checkout_button(self):
        add_to_cart_modal_proceed_to_checkout = \
            Button(self.driver,
                   xpath="//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span")
        add_to_cart_modal_proceed_to_checkout.click()

    def click_add_to_cart_modal_x_button(self):
        add_to_cart_modal_x = Button(self.driver,
                                     xpath="//*[@title='Close window']")
        add_to_cart_modal_x.click()
