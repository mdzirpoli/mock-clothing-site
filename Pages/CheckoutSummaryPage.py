"""
Created on February 29, 2020

@author: Mark Zirpoli

This module contains methods for the Checkout Summary page
"""
from selenium.webdriver.common.by import By


class CheckoutSummaryPage(object):
    """
    Page object for Checkout Summary page
    """

    # Checkout Summary page locators
    CHECKOUT_SUMMARY_QUANTITY_TEXTBOX = (By.XPATH, "//*[@id='product_2_7_0_272223']/td[5]/input[2]")
    CHECKOUT_SUMMARY_QUANTITY_MINUS_BUTTON = (By.XPATH, "//*[@id='cart_quantity_down_2_7_0_272223']/span/i")
    CHECKOUT_SUMMARY_QUANTITY_PLUS_BUTTON = (By.XPATH, "//*[@id='cart_quantity_up_2_7_0_272223']/span")
    CHECKOUT_SUMMARY_TRASHCAN_BUTTON = (By.XPATH, "//*[@id='2_7_0_272223']/i")
    CHECKOUT_SUMMARY_PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//*[@id='center_column']/p[2]/a[1]/span")
    CHECKOUT_SUMMARY_CONTINUE_SHOPPING_LINK = (By.XPATH, "//*[@id='center_column']/p[2]/a[2]")

    def __init__(self, driver):
        self.driver = driver

    def input_checkout_summary_quantity_textbox(self, quantity):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_QUANTITY_TEXTBOX).clear()
        self.driver.find_element(*self.CHECKOUT_SUMMARY_QUANTITY_TEXTBOX).send_keys(quantity)

    def click_checkout_summary_minus_button(self):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_QUANTITY_MINUS_BUTTON).click()

    def click_checkout_summary_plus_button(self):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_QUANTITY_PLUS_BUTTON).click()

    def click_checkout_summary_trashcan_button(self):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_TRASHCAN_BUTTON).click()

    def click_checkout_summary_proceed_to_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_PROCEED_TO_CHECKOUT_BUTTON).click()

    def click_checkout_summary_continue_shopping_link(self):
        self.driver.find_element(*self.CHECKOUT_SUMMARY_CONTINUE_SHOPPING_LINK).click()
