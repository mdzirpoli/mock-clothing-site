"""
Created on November 16, 2019

@author: Mark Zirpoli

This module contains methods for the Sign In page
"""


class SignInPage(object):

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_menu_button_xpath = "//*[@id='header']/div[2]/div/div/nav/div[1]/a"
        self.create_account_email_address_textbox_id = "email_create"
        self.create_an_account_button_id = "SubmitCreate"
        self.email_address_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.sign_in_button_id = "SubmitLogin"
        self.forgot_your_password_link_xpath = "//*[@id='login_form']/div/p[1]/a"

    def click_sign_in_menu_button(self):
        self.driver.find_element_by_xpath(self.sign_in_menu_button_xpath).click()

    def input_create_account_email_address_textbox(self, email):
        self.driver.find_element_by_id(self.create_account_email_address_textbox_id).send_keys(email)

    def click_create_an_account_button(self):
        self.driver.find_element_by_id(self.create_an_account_button_id).click()

    def input_email_address_textbox(self, email):
        self.driver.find_element_by_id(self.email_address_textbox_id).send_keys(email)

    def input_password_textbox(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element_by_id(self.sign_in_button_id).click()

    def click_forgot_your_password_link(self):
        self.driver.find_element_by_xpath(self.forgot_your_password_link_xpath).click()
