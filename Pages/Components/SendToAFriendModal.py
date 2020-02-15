"""
Created on February 15, 2020

@author: Mark Zirpoli

This module contains methods for the Send To A Friend modal
"""

from selenium.webdriver.common.by import By


class SendToAFriendModal(object):
    """
    Page object for Send To A Friend Modal
    """

    # Send To a Friend Modal locators
    SEND_TO_A_FRIEND_LINK = (By.ID, "send_friend_button")
    NAME_OF_YOUR_FRIEND_TEXTBOX = (By.ID, "friend_name")
    EMAIL_ADDRESS_OF_YOUR_FRIEND_TEXTBOX = (By.ID, "friend_email")
    SEND_TO_A_FRIEND_SEND_BUTTON = (By.ID, "sendEmail")
    SEND_TO_A_FRIEND_CANCEL_BUTTON = (By.XPATH, "//*[@id='send_friend_form_content']/p/a")
    SEND_TO_A_FRIEND_X_BUTTON = (By.XPATH, "//*[@title='Close']")

    def __init__(self, driver):
        self.driver = driver

    def click_send_to_a_friend_link(self):
        self.driver.find_element(*self.SEND_TO_A_FRIEND_LINK).click()

    def input_name_of_your_friend_textbox(self, friend):
        self.driver.find_element(*self.NAME_OF_YOUR_FRIEND_TEXTBOX).send_keys(friend)

    def input_email_address_of_your_friend_textbox(self, email):
        self.driver.find_element(*self.EMAIL_ADDRESS_OF_YOUR_FRIEND_TEXTBOX).send_keys(email)

    def click_send_to_a_friend_send_button(self):
        self.driver.find_element(*self.SEND_TO_A_FRIEND_SEND_BUTTON).click()

    def click_send_to_a_friend_cancel_button(self):
        self.driver.find_element(*self.SEND_TO_A_FRIEND_CANCEL_BUTTON).click()

    def click_send_to_a_friend_x_button(self):
        self.driver.find_element(*self.SEND_TO_A_FRIEND_X_BUTTON).click()
