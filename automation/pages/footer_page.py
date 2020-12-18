"""
Created on February 2, 2020
Modified on December 18, 2020

@author: Mark Zirpoli

This module contains methods for the Footer links
"""

from automation.elements import Link, TextField


class FooterPage(object):
    """
    Page object for Footer links
    """
    def __init__(self, driver):
        self.driver = driver

    def input_newsletter_email_textbox(self, email):
        newsletter_email = TextField(self.driver, div_id="newsletter-input")
        newsletter_email.input_text(email)

    def click_follow_us_facebook_link(self):
        follow_us_facebook = Link(self.driver, xpath="//*[span='Facebook']")
        follow_us_facebook.click()

    def click_follow_us_twitter_link(self):
        follow_us_twitter = Link(self.driver, xpath="//*[span='Twitter']")
        follow_us_twitter.click()

    def click_follow_us_youtube_link(self):
        follow_us_youtube = Link(self.driver, xpath="//*[span='Youtube']")
        follow_us_youtube.click()

    def click_follow_us_google_plus_link(self):
        follow_us_google_plus = Link(self.driver,
                                     xpath="//*[span='Google Plus']")
        follow_us_google_plus.click()

    def click_categories_women_link(self):
        categories_women = \
            Link(self.driver,
                 xpath="//*[@id='footer']/div/section[2]/div/div/ul/li/a")
        categories_women.click()

    def click_information_specials_link(self):
        information_specials = Link(self.driver,
                                    xpath="//*[@title='Specials']")
        information_specials.click()

    def click_information_new_products_link(self):
        information_new_products = Link(self.driver,
                                        xpath="//*[@title='New products']")
        information_new_products.click()

    def click_information_best_sellers_link(self):
        information_best_sellers = Link(self.driver,
                                        xpath="//*[@title='Best sellers']")
        information_best_sellers.click()

    def click_information_our_stores_link(self):
        information_our_stories = Link(self.driver,
                                       xpath="//*[@title='Our stores']")
        information_our_stories.click()

    def click_information_contact_us_link(self):
        information_contact_us = Link(self.driver,
                                      xpath="//*[@title='Contact us']")
        information_contact_us.click()

    def click_information_terms_and_conditions_of_use_link(self):
        information_terms_and_conditions_of_use = \
            Link(self.driver,
                 xpath="//*[@title='Terms and conditions of use']")
        information_terms_and_conditions_of_use.click()

    def click_information_about_us_link(self):
        information_about_us = Link(self.driver,
                                    xpath="//*[@title='About us']")
        information_about_us.click()

    def click_information_sitemap_link(self):
        information_sitemap = Link(self.driver, xpath="//*[@title='Sitemap']")
        information_sitemap.click()

    def click_my_account_my_orders_link(self):
        my_account_my_orders = Link(self.driver,
                                    xpath="//*[@title='My orders']")
        my_account_my_orders.click()

    def click_my_account_my_credit_slips_link(self):
        my_account_my_credit_slips = \
            Link(self.driver, xpath="//*[@title='My credit slips']")
        my_account_my_credit_slips.click()

    def click_my_account_my_addresses_link(self):
        my_account_my_addresses = Link(self.driver,
                                       xpath="//*[@title='My addresses']")
        my_account_my_addresses.click()

    def click_my_account_my_personal_info_link(self):
        my_account_my_personal_info = \
            Link(self.driver,
                 xpath="//*[@title='Manage my personal information']")
        my_account_my_personal_info.click()
