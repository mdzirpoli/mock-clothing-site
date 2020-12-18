"""
Created on February 16, 2020
Modified on December 18, 2020

@author: Mark Zirpoli

This module contains methods for My Account page
"""

from automation.elements import Button


class MyAccountPage(object):
    """
    Page object for My Account page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_order_history_and_details_button(self):
        order_history_and_details = \
            Button(self.driver,
                   xpath="//span[text()='Order history and details']")
        order_history_and_details.click()

    def click_my_wishlists_button(self):
        my_wishlists = Button(self.driver,
                              xpath="//span[text()='My wishlists']")
        my_wishlists.click()

    def click_my_credit_slips_button(self):
        my_credit_slips = Button(self.driver,
                                 xpath="//span[text()='My credit slips']")
        my_credit_slips.click()

    def click_my_addresses_button(self):
        my_addresses = Button(self.driver,
                              xpath="//span[text()='My addresses']")
        my_addresses.click()

    def click_my_personal_information_button(self):
        my_personal_information = \
            Button(self.driver,
                   xpath="//span[text()='My personal information']")
        my_personal_information.click()
