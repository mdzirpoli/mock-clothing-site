"""
Created on November 16, 2019
Modified on November 29, 2020

@author: Mark Zirpoli

This module contains methods for the Sign In page
"""
from automation.elements import Button, TextField


class SignInPage(object):
    """
    Page object for Sign In page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_sign_in_menu_button(self):
        sign_in = Button(self.driver,
                         xpath="//*[@id='header']/div[2]/div/div/nav/div[1]/a")
        sign_in.click()

    def input_create_account_email_address_textbox(self, email):
        input_email = TextField(self.driver, div_id="email_create")
        input_email.input_text(email)

    def click_create_an_account_button(self):
        create_account_button = Button(self.driver, div_id="SubmitCreate")
        create_account_button.click()

    def input_email_address_textbox(self, email):
        input_email_address = TextField(self.driver, div_id="email")
        input_email_address.input_text(email)

    def input_password_textbox(self, password):
        input_password = TextField(self.driver, div_id="passwd")
        input_password.input_text(password)

    def click_sign_in_button(self):
        sign_in_button = Button(self.driver, div_id="SubmitLogin")
        sign_in_button.click()

    def click_forgot_your_password_link(self):
        forgot_password = Button(self.driver,
                                 xpath="//*[@id='login_form']/div/p[1]/a")
        forgot_password.click()
