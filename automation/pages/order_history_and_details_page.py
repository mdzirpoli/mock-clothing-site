"""
Created on April 4, 2020

@author: Mark Zirpoli

This module contains methods for the Order History And Details page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OrderHistoryAndDetailsPage(object):
    """
    Page object for Order History And Details page
    """

    # Order History And Details page locators
    ORDER_HISTORY_ORDER_REFERENCE_LINK = (By.XPATH, "//*[@id='order-list']/tbody/tr/td[1]/a")
    ORDER_HISTORY_INVOICE_PDF_LINK = (By.XPATH, "//*[@title='Invoice']")
    ORDER_HISTORY_DETAILS_BUTTON = (By.XPATH, "//*[@id='order-list']/tbody/tr/td[7]/a[1]/span")
    ORDER_HISTORY_REORDER_LINK = (By.XPATH, "//*[@title='Reorder']")
    ORDER_HISTORY_BACK_TO_YOUR_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='center_column']/ul/li[1]/a/span")
    ORDER_HISTORY_HOME_BUTTON = (By.XPATH, "//*[@id='center_column']/ul/li[2]/a/span")
    ORDER_HISTORY_ORDER_REFERENCE_REORDER_BUTTON = (By.XPATH, "//span[text()='Reorder']")
    ORDER_HISTORY_ORDER_REFERENCE_DOWNLOAD_YOUR_INVOICE = (By.XPATH, "//*[@id='block-order-detail']/div[2]/p[3]/a")
    ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_DROPDOWN = (By.NAME, "id_product")
    ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_TEXTBOX = (By.NAME, "msgText")
    ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_SEND_BUTTON = (By.XPATH, "//span[text()='Send']")

    def __init__(self, driver):
        self.driver = driver

    def click_order_history_order_reference_link(self):
        self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_LINK).click()

    def click_order_history_order_reference_reorder_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_REORDER_BUTTON).click()

    def click_order_history_order_reference_download_your_invoice_as_pdf(self):
        self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_DOWNLOAD_YOUR_INVOICE).click()

    def select_order_history_order_reference_product_message_dropdown(self, product):
        dropdown = Select(self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_DROPDOWN))
        dropdown.select_by_visible_text(product)

    def input_order_history_order_reference_product_message_textbox(self, textbox):
        self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_TEXTBOX).send_keys(textbox)

    def click_order_history_order_reference_product_message_send_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_ORDER_REFERENCE_PRODUCT_MESSAGE_SEND_BUTTON).click()

    def click_order_history_invoice_pdf_link(self):
        self.driver.find_element(*self.ORDER_HISTORY_INVOICE_PDF_LINK).click()

    def click_order_history_details_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_DETAILS_BUTTON).click()

    def click_order_history_reorder_link(self):
        self.driver.find_element(*self.ORDER_HISTORY_REORDER_LINK).click()

    def click_order_history_back_to_your_account_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_BACK_TO_YOUR_ACCOUNT_BUTTON).click()

    def click_order_history_home_button(self):
        self.driver.find_element(*self.ORDER_HISTORY_HOME_BUTTON).click()
