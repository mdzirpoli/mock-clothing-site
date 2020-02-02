"""
Created on February 2, 2020

@author: Mark Zirpoli

This module contains methods for the Footer links
"""

from selenium.webdriver.common.by import By


class FooterPage(object):
    """
    Page object for Footer links
    """

    # Footer page locators
    NEWSLETTER_EMAIL_TEXTBOX = (By.ID, "newsletter-input")
    FOLLOW_US_FACEBOOK_LINK = (By.XPATH, "//*[span='Facebook']")
    FOLLOW_US_TWITTER_LINK = (By.XPATH, "//*[span='Twitter']")
    FOLLOW_US_YOUTUBE_LINK = (By.XPATH, "//*[span='Youtube']")
    FOLLOW_US_GOOGLE_PLUS_LINK = (By.XPATH, "//*[span='Google Plus']")
    CATEGORIES_WOMEN_LINK = (By.XPATH, "//*[@id='footer']/div/section[2]/div/div/ul/li/a")
    INFORMATION_SPECIALS_LINK = (By.XPATH, "//*[@title='Specials']")
    INFORMATION_NEW_PRODUCTS_LINK = (By.XPATH, "//*[@title='New products']")
    INFORMATION_BEST_SELLERS_LINK = (By.XPATH, "//*[@title='Best sellers']")
    INFORMATION_OUR_STORES_LINK = (By.XPATH, "//*[@title='Our stores']")
    INFORMATION_CONTACT_US_LINK = (By.XPATH, "//*[@title='Contact us']")
    INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK = (By.XPATH, "//*[@title='Terms and conditions of use']")
    INFORMATION_ABOUT_US_LINK = (By.XPATH, "//*[@title='About us']")
    INFORMATION_SITEMAP_LINK = (By.XPATH, "//*[@title='Sitemap']")
    MY_ACCOUNT_MY_ORDERS_LINK = (By.XPATH, "//*[@title='My orders']")
    MY_ACCOUNT_MY_CREDIT_SLIPS_LINK = (By.XPATH, "//*[@title='My credit slips']")
    MY_ACCOUNT_MY_ADDRESSES_LINK = (By.XPATH, "//*[@title='My addresses']")
    MY_ACCOUNT_MY_PERSONAL_INFO_LINK = (By.XPATH, "//*[@title='Manage my personal information']")

    def __init__(self, driver):
        self.driver = driver

    def input_newsletter_email_textbox(self, email):
        self.driver.find_element(*self.NEWSLETTER_EMAIL_TEXTBOX).send_keys(email)

    def click_follow_us_facebook_link(self):
        self.driver.find_element(*self.FOLLOW_US_FACEBOOK_LINK).click()

    def click_follow_us_twitter_link(self):
        self.driver.find_element(*self.FOLLOW_US_TWITTER_LINK).click()

    def click_follow_us_youtube_link(self):
        self.driver.find_element(*self.FOLLOW_US_YOUTUBE_LINK).click()

    def click_follow_us_google_plus_link(self):
        self.driver.find_element(*self.FOLLOW_US_GOOGLE_PLUS_LINK).click()

    def click_categories_women_link(self):
        self.driver.find_element(*self.CATEGORIES_WOMEN_LINK).click()

    def click_information_specials_link(self):
        self.driver.find_element(*self.INFORMATION_SPECIALS_LINK).click()

    def click_information_new_products_link(self):
        self.driver.find_element(*self.INFORMATION_NEW_PRODUCTS_LINK).click()

    def click_information_best_sellers_link(self):
        self.driver.find_element(*self.INFORMATION_BEST_SELLERS_LINK).click()

    def click_information_our_stores_link(self):
        self.driver.find_element(*self.INFORMATION_OUR_STORES_LINK).click()

    def click_information_contact_us_link(self):
        self.driver.find_element(*self.INFORMATION_CONTACT_US_LINK).click()

    def click_information_terms_and_conditions_of_use_link(self):
        self.driver.find_element(*self.INFORMATION_TERMS_AND_CONDITION_OF_USE_LINK).click()

    def click_information_about_us_link(self):
        self.driver.find_element(*self.INFORMATION_ABOUT_US_LINK).click()

    def click_information_sitemap_link(self):
        self.driver.find_element(*self.INFORMATION_SITEMAP_LINK).click()

    def click_my_account_my_orders_link(self):
        self.driver.find_element(*self.MY_ACCOUNT_MY_ORDERS_LINK).click()

    def click_my_account_my_credit_slips_link(self):
        self.driver.find_element(*self.MY_ACCOUNT_MY_CREDIT_SLIPS_LINK).click()

    def click_my_account_my_addresses_link(self):
        self.driver.find_element(*self.MY_ACCOUNT_MY_ADDRESSES_LINK).click()

    def click_my_account_my_personal_info_link(self):
        self.driver.find_element(*self.MY_ACCOUNT_MY_PERSONAL_INFO_LINK).click()
