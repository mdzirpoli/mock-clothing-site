"""
Created on February 4, 2020
Modified on December 21, 2020

@author: Mark Zirpoli

This module contains methods for the Create An Account page
"""

from automation.elements import TextField, Button, DropDown, CheckBox


class CreateAnAccountPage(object):
    """
    Page object for Create An Account page
    """
    def __init__(self, driver):
        self.driver = driver

    def select_title_mr_radio_button(self):
        title_mr_radio = Button(self.driver, div_id="id_gender1")
        title_mr_radio.click()

    def select_title_mrs_radio_button(self):
        title_mrs_radio = Button(self.driver, div_id="id_gender2")
        title_mrs_radio.click()

    def input_your_personal_information_first_name_textbox(self, first_name):
        personal_information_first_name = \
            TextField(self.driver, div_id="customer_firstname")
        personal_information_first_name.input_text(first_name)

    def input_your_personal_information_last_name_textbox(self, last_name):
        personal_information_last_name = \
            TextField(self.driver, div_id="customer_lastname")
        personal_information_last_name.input_text(last_name)

    def input_your_personal_information_email_textbox(self, email):
        personal_information_email = TextField(self.driver, div_id="email")
        personal_information_email.input_text(email)

    def input_your_personal_information_password_textbox(self, password):
        personal_information_password = TextField(self.driver, div_id="passwd")
        personal_information_password.input_text(password)

    def select_date_of_birth_days_dropdown(self, days):
        date_of_birth_days = DropDown(self.driver, div_id="days")
        date_of_birth_days.select_dropdown(days)

    def select_date_of_birth_month_dropdown(self, month):
        date_of_birth_month = DropDown(self.driver, div_id="months")
        date_of_birth_month.select_dropdown(month)

    def select_date_of_birth_year_dropdown(self, year):
        date_of_birth_year = DropDown(self.driver, div_id="years")
        date_of_birth_year.select_dropdown(year)

    def check_newsletter_checkbox(self):
        check_newsletter = CheckBox(self.driver, div_id="newsletter")
        check_newsletter.check()

    def uncheck_newsletter_checkbox(self):
        uncheck_newsletter = CheckBox(self.driver, div_id="newsletter")
        uncheck_newsletter.uncheck()

    def check_special_offers_checkbox(self):
        check_special_offers = CheckBox(self.driver, div_id="optin")
        check_special_offers.check()

    def uncheck_special_offers_checkbox(self):
        uncheck_special_offers = CheckBox(self.driver, div_id="optin")
        uncheck_special_offers.uncheck()

    def input_your_address_first_name_textbox(self, first_name):
        address_first_name = TextField(self.driver, div_id="firstname")
        address_first_name.input_text(first_name)

    def input_your_address_last_name_textbox(self, last_name):
        address_last_name = TextField(self.driver, div_id="lastname")
        address_last_name.input_text(last_name)

    def input_your_address_company_textbox(self, company):
        address_company = TextField(self.driver, div_id="company")
        address_company.input_text(company)

    def input_your_address_address_textbox(self, address):
        address_address = TextField(self.driver, div_id="address1")
        address_address.input_text(address)

    def input_your_address_line_two_textbox(self, address_two):
        address_line_two = TextField(self.driver, div_id="address2")
        address_line_two.input_text(address_two)

    def input_your_address_city_textbox(self, city):
        address_city = TextField(self.driver, div_id="city")
        address_city.input_text(city)

    def select_your_address_state_dropdown(self, state):
        address_state = DropDown(self.driver, div_id="id_state")
        address_state.select_dropdown(state)

    def input_your_address_zip_postal_code_textbox(self, zip_code):
        address_zip_postal_code = TextField(self.driver, div_id="postcode")
        address_zip_postal_code.input_text(zip_code)

    def select_your_address_country_dropdown(self, country):
        address_country = DropDown(self.driver, div_id="id_country")
        address_country.select_dropdown(country)

    def input_your_address_additional_information_textbox(self, additional_info):
        address_additional_information = TextField(self.driver, div_id="other")
        address_additional_information.input_text(additional_info)

    def input_your_address_home_phone_textbox(self, home_phone):
        address_home_phone = TextField(self.driver, div_id="phone")
        address_home_phone.input_text(home_phone)

    def input_your_address_mobile_phone_textbox(self, mobile_phone):
        address_mobile_phone = TextField(self.driver, div_id="phone_mobile")
        address_mobile_phone.input_text(mobile_phone)

    def input_your_address_alias_textbox(self, alias):
        address_alias = TextField(self.driver, div_id="alias")
        address_alias.input_text(alias)

    def click_your_address_register_button(self):
        address_register = Button(self.driver,
                                  xpath="//*[span='Register']")
        address_register.click()
