"""
Created on February 16, 2020

@author: Mark Zirpoli

This module contains methods for My Account page
"""
from selenium.webdriver.common.by import By


class MyAccountPage(object):
    """
    Page object for My Account page
    """

    # My Account page locators
    ORDER_HISTORY_AND_DETAILS_BUTTON = (By.XPATH, "//span[text()='Order history and details']")
    MY_WISHLISTS_BUTTON = (By.XPATH, "//span[text()='My wishlists']")
    MY_CREDIT_SLIPS_BUTTON = (By.XPATH, "//span[text()='My credit slips']")
    MY_ADDRESSES_BUTTON = (By.XPATH, "//span[text()='My addresses']")
    MY_PERSONAL_INFORMATION_BUTTON = (By.XPATH, "//span[text()='My personal information']")

    def __init__(self, driver):
        self.driver = driver

    def click_order_history_and_details_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_AND_DETAILS_BUTTON).click()

    def click_my_wishlists_button(self):
        self.driver.find_element(*self.MY_WISHLISTS_BUTTON).click()

    def click_my_credit_slips_button(self):
        self.driver.find_element(*self.MY_CREDIT_SLIPS_BUTTON).click()

    def click_my_addresses_button(self):
        self.driver.find_element(*self.MY_ADDRESSES_BUTTON).click()

    def click_my_personal_information_button(self):
        self.driver.find_element(*self.MY_PERSONAL_INFORMATION_BUTTON).click()
