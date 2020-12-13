"""
Created on April 4, 2020
Modified on December 13, 2020

@author: Mark Zirpoli

This module contains methods for the Order History And Details page
"""

from automation.elements import Button, Link, TextField, DropDown


class OrderHistoryAndDetailsPage(object):
    """
    Page object for Order History And Details page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_order_history_order_reference_link(self):
        order_history_order_reference = \
            Link(self.driver, xpath="//*[@id='order-list']/tbody/tr/td[1]/a")
        order_history_order_reference.click()

    def click_order_history_order_reference_reorder_button(self):
        order_history_order_reference_reorder = \
                Button(self.driver, xpath="//span[contains(.,'Reorder')]")
        order_history_order_reference_reorder.click()

    def click_order_history_order_reference_download_your_invoice_as_pdf(self):
        order_history_order_reference_download = \
            Link(self.driver,
                 xpath="//a[contains(.,'Download your invoice as a PDF file.')]")
        order_history_order_reference_download.click()

    def select_order_history_order_reference_product_message_dropdown(self, product):
        order_history_order_reference_product_message = \
            DropDown(self.driver, div_name="id_product")
        order_history_order_reference_product_message.select_dropdown(product)

    def input_order_history_order_reference_product_message_textbox(self, textbox):
        order_history_order_reference_product_message = \
            TextField(self.driver, div_name="msgText")
        order_history_order_reference_product_message.input_text(textbox)

    def click_order_history_order_reference_product_message_send_button(self):
        order_history_order_reference_product_message_send = \
            Button(self.driver, xpath="//span[text()='Send']")
        order_history_order_reference_product_message_send.click()

    def click_order_history_invoice_pdf_link(self):
        order_history_invoice_pdf = \
            Link(self.driver, xpath="(//a[@title='Invoice'])[1]")
        order_history_invoice_pdf.click()

    def click_order_history_details_button(self):
        order_history_details = \
            Button(self.driver,
                   xpath="//*[@id='order-list']/tbody/tr/td[7]/a[1]/span")
        order_history_details.click()

    def click_order_history_reorder_link(self):
        order_history_reorder = \
            Link(self.driver, xpath="(//a[@title='Reorder'])[1]")
        order_history_reorder.click()

    def click_order_history_back_to_your_account_button(self):
        order_history_back_to_your_account = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/ul/li[1]/a/span")
        order_history_back_to_your_account.click()

    def click_order_history_home_button(self):
        order_history_home = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/ul/li[2]/a/span")
        order_history_home.click()
