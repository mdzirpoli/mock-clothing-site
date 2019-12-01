"""
Created on November 24, 2019

@author: Mark Zirpoli

This module contains methods for the Contact Us page
"""

from Pages.BasePageObject import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ContactUsPage(BasePage):
    """
    Page object for Contact Us page
    """

    # Contact Us page locators
    CONTACT_US_MENU_BUTTON = (By.XPATH, "//*[@id='contact-link']/a")
    SUBJECT_HEADING_DROPDOWN = (By.ID, "id_contact")
    CONTACT_US_EMAIL_ADDRESS_TEXTBOX = (By.ID, "email")
    ORDER_REFERENCE_TEXTBOX = (By.ID, "id_order")
    ATTACH_FILE_UPLOAD_BUTTON = (By.ID, "fileUpload")
    CONTACT_US_MESSAGE_TEXTBOX = (By.ID, "message")
    CONTACT_US_SEND_BUTTON = (By.ID, "submitMessage")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_contact_us_menu_button(self):
        self.driver.find_element(*ContactUsPage.CONTACT_US_MENU_BUTTON).click()

    def click_subject_heading_dropdown(self, value):
        dropdown = Select(self.driver.find_element(*ContactUsPage.SUBJECT_HEADING_DROPDOWN))
        dropdown.select_by_visible_text(value)

    def input_contact_us_email_address_textbox(self, email):
        self.driver.find_element(*ContactUsPage.CONTACT_US_EMAIL_ADDRESS_TEXTBOX).send_keys(email)

    def input_order_reference_textbox(self, order):
        self.driver.find_element(*ContactUsPage.ORDER_REFERENCE_TEXTBOX).send_keys(order)

    def attach_file_upload(self, path):
        self.driver.find_element(*ContactUsPage.ATTACH_FILE_UPLOAD_BUTTON).send_keys(path)

    def input_contact_us_message_textbox(self, message):
        self.driver.find_element(*ContactUsPage.CONTACT_US_MESSAGE_TEXTBOX).send_keys(message)

    def click_contact_us_send_button(self):
        self.driver.find_element(*ContactUsPage.CONTACT_US_SEND_BUTTON).click()
