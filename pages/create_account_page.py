"""
Created on February 4, 2020

@author: Mark Zirpoli

This module contains methods for the Create An Account page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreateAnAccountPage(object):
    """
    Page object for Create An Account page
    """

    # Create An Account page locators

    # Your Personal Information locators
    YOUR_PERSONAL_INFORMATION_TITLE_MR_RADIO_BUTTON = (By.ID, "id_gender1")
    YOUR_PERSONAL_INFORMATION_TITLE_MRS_RADIO_BUTTON = (By.ID, "id_gender2")
    YOUR_PERSONAL_INFORMATION_FIRST_NAME_TEXTBOX = (By.ID, "customer_firstname")
    YOUR_PERSONAL_INFORMATION_LAST_NAME_TEXTBOX = (By.ID, "customer_lastname")
    YOUR_PERSONAL_INFORMATION_EMAIL_TEXTBOX = (By.ID, "email")
    YOUR_PERSONAL_INFORMATION_PASSWORD_TEXTBOX = (By.ID, "passwd")
    YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_DAYS_DROPDOWN = (By.ID, "days")
    YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_MONTH_DROPDOWN = (By.ID, "months")
    YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_YEAR_DROPDOWN = (By.ID, "years")
    YOUR_PERSONAL_INFORMATION_NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    YOUR_PERSONAL_INFORMATION_SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")

    # Your Address page locators
    YOUR_ADDRESS_FIRST_NAME_TEXTBOX = (By.ID, "firstname")
    YOUR_ADDRESS_LAST_NAME_TEXTBOX = (By.ID, "lastname")
    YOUR_ADDRESS_COMPANY_TEXTBOX = (By.ID, "company")
    YOUR_ADDRESS_ADDRESS_TEXTBOX = (By.ID, "address1")
    YOUR_ADDRESS_ADDRESS_LINE_TWO_TEXTBOX = (By.ID, "address2")
    YOUR_ADDRESS_CITY_TEXTBOX = (By.ID, "city")
    YOUR_ADDRESS_STATE_DROPDOWN = (By.ID, "id_state")
    YOUR_ADDRESS_ZIP_POSTAL_CODE_TEXTBOX = (By.ID, "postcode")
    YOUR_ADDRESS_COUNTRY_DROPDOWN = (By.ID, "id_country")
    YOUR_ADDRESS_ADDITIONAL_INFORMATION_TEXTBOX = (By.ID, "other")
    YOUR_ADDRESS_HOME_PHONE_TEXTBOX = (By.ID, "phone")
    YOUR_ADDRESS_MOBILE_PHONE_TEXTBOX = (By.ID, "phone_mobile")
    YOUR_ADDRESS_ALIAS_TEXTBOX = (By.ID, "alias")
    YOUR_ADDRESS_REGISTER_BUTTON = (By.XPATH, "//*[span='Register']")

    def __init__(self, driver):
        self.driver = driver

    def select_title_mr_radio_button(self):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_TITLE_MR_RADIO_BUTTON).click()

    def select_title_mrs_radio_button(self):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_TITLE_MRS_RADIO_BUTTON).click()

    def input_your_personal_information_first_name_textbox(self, first_name):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_FIRST_NAME_TEXTBOX).send_keys(first_name)

    def input_your_personal_information_last_name_textbox(self, last_name):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_LAST_NAME_TEXTBOX).send_keys(last_name)

    def input_your_personal_information_email_textbox(self, email):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_EMAIL_TEXTBOX).clear()
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_EMAIL_TEXTBOX).send_keys(email)

    def input_your_personal_information_password_textbox(self, password):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_PASSWORD_TEXTBOX).send_keys(password)

    def select_date_of_birth_days_dropdown(self, days):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_DAYS_DROPDOWN).send_keys(days)

    def select_date_of_birth_month_dropdown(self, month):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_MONTH_DROPDOWN).send_keys(month)

    def select_date_of_birth_year_dropdown(self, year):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_DATE_OF_BIRTH_YEAR_DROPDOWN).send_keys(year)

    def click_newsletter_checkbox(self):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_NEWSLETTER_CHECKBOX).click()

    def click_special_offers_checkbox(self):
        self.driver.find_element(*self.YOUR_PERSONAL_INFORMATION_SPECIAL_OFFERS_CHECKBOX).click()

    def input_your_address_first_name_textbox(self, first_name):
        self.driver.find_element(*self.YOUR_ADDRESS_FIRST_NAME_TEXTBOX).send_keys(first_name)

    def input_your_address_last_name_textbox(self, last_name):
        self.driver.find_element(*self.YOUR_ADDRESS_LAST_NAME_TEXTBOX).send_keys(last_name)

    def input_your_address_company_textbox(self, company):
        self.driver.find_element(*self.YOUR_ADDRESS_COMPANY_TEXTBOX).send_keys(company)

    def input_your_address_address_textbox(self, address):
        self.driver.find_element(*self.YOUR_ADDRESS_ADDRESS_TEXTBOX).send_keys(address)

    def input_your_address_line_two_textbox(self, address_two):
        self.driver.find_element(*self.YOUR_ADDRESS_ADDRESS_LINE_TWO_TEXTBOX).send_keys(address_two)

    def input_your_address_city_textbox(self, city):
        self.driver.find_element(*self.YOUR_ADDRESS_CITY_TEXTBOX).send_keys(city)

    def select_your_address_state_dropdown(self, state):
        dropdown = Select(self.driver.find_element(*self.YOUR_ADDRESS_STATE_DROPDOWN))
        dropdown.select_by_visible_text(state)

    def input_your_address_zip_postal_code_textbox(self, zip):
        self.driver.find_element(*self.YOUR_ADDRESS_ZIP_POSTAL_CODE_TEXTBOX).send_keys(zip)

    def select_your_address_country_dropdown(self, country):
        dropdown = Select(self.driver.find_element(*self.YOUR_ADDRESS_COUNTRY_DROPDOWN))
        dropdown.select_by_visible_text(country)

    def input_your_address_additional_information_textbox(self, additional_info):
        self.driver.find_element(*self.YOUR_ADDRESS_ADDITIONAL_INFORMATION_TEXTBOX).send_keys(additional_info)

    def input_your_address_home_phone_textbox(self, home_phone):
        self.driver.find_element(*self.YOUR_ADDRESS_HOME_PHONE_TEXTBOX).send_keys(home_phone)

    def input_your_address_mobile_phone_textbox(self, mobile_phone):
        self.driver.find_element(*self.YOUR_ADDRESS_MOBILE_PHONE_TEXTBOX).send_keys(mobile_phone)

    def input_your_address_alias_textbox(self, alias):
        self.driver.find_element(*self.YOUR_ADDRESS_ALIAS_TEXTBOX).clear()
        self.driver.find_element(*self.YOUR_ADDRESS_ALIAS_TEXTBOX).send_keys(alias)

    def click_your_address_register_button(self):
        self.driver.find_element(*self.YOUR_ADDRESS_REGISTER_BUTTON).click()


