"""
Created on November 24, 2019
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Contact Us page
"""

from automation.elements import Button, TextField, DropDown


class ContactUsPage(object):
    """
    Page object for Contact Us page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_contact_us_menu_button(self):
        contact_us_menu = Button(self.driver,
                                 xpath="//*[@id='contact-link']/a")
        contact_us_menu.click()

    def click_subject_heading_dropdown(self, value):
        subject_header = DropDown(self.driver, div_id="id_contact")
        subject_header.select_dropdown(value)

    def input_contact_us_email_address_textbox(self, email):
        contact_us_email_address = TextField(self.driver, div_id="email")
        contact_us_email_address.input_text(email)

    def input_order_reference_textbox(self, order):
        order_reference = TextField(self.driver, div_id="id_order")
        order_reference.input_text(order)

    def attach_file_upload(self, path):
        attach_file = TextField(self.driver, div_id="fileUpload")
        attach_file.input_text(path)

    def input_contact_us_message_textbox(self, message):
        contact_us_message = TextField(self.driver, div_id="message")
        contact_us_message.input_text(message)

    def click_contact_us_send_button(self):
        contact_us = Button(self.driver, div_id="submitMessage")
        contact_us.click()
