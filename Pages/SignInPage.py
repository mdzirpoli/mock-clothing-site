"""
Created on November 16, 2019

@author: Mark Zirpoli

This module contains methods for the Sign In page
"""
from selenium.webdriver.common.by import By


class SignInPage(object):
    """
    Page object for Sign In page
    """

    # Sign In page locators
    SIGN_IN_MENU_BUTTON = (By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[1]/a")
    CREATE_ACCOUNT_EMAIL_ADDRESS_TEXTBOX = (By.ID, "email_create")
    CREATE_AN_ACCOUNT_BUTTON = (By.ID, "SubmitCreate")
    EMAIL_ADDRESS_TEXTBOX = (By.ID, "email")
    PASSWORD_TEXTBOX = (By.ID, "passwd")
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")
    FORGOT_YOUR_PASSWORD_LINK = (By.XPATH, "//*[@id='login_form']/div/p[1]/a")

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in_menu_button(self):
        self.driver.find_element(*self.SIGN_IN_MENU_BUTTON).click()

    def input_create_account_email_address_textbox(self, email):
        self.driver.find_element(*self.CREATE_ACCOUNT_EMAIL_ADDRESS_TEXTBOX).send_keys(email)

    def click_create_an_account_button(self):
        self.driver.find_element(*self.CREATE_AN_ACCOUNT_BUTTON).click()

    def input_email_address_textbox(self, email):
        self.driver.find_element(*self.EMAIL_ADDRESS_TEXTBOX).send_keys(email)

    def input_password_textbox(self, password):
        self.driver.find_element(*self.PASSWORD_TEXTBOX).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def click_forgot_your_password_link(self):
        self.driver.find_element(*self.FORGOT_YOUR_PASSWORD_LINK).click()
