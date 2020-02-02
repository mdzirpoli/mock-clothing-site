"""
Created on February 2, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Footer links
"""

from Pages.FooterPage import FooterPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class FooterPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.footer = FooterPage(self.driver)

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_newsletter_email_textbox(self):
        self.footer.input_newsletter_email_textbox("joesmith@email.com")

    @unittest.skip("pass")
    def test_click_follow_us_facebook_link(self):
        self.footer.click_follow_us_facebook_link()

    @unittest.skip("pass")
    def test_click_follow_us_twitter_link(self):
        self.footer.click_follow_us_twitter_link()

    @unittest.skip("pass")
    def test_click_follow_us_youtube_link(self):
        self.footer.click_follow_us_youtube_link()

    @unittest.skip("pass")
    def test_click_follow_us_google_plus_link(self):
        self.footer.click_follow_us_google_plus_link()

    @unittest.skip("pass")
    def test_click_categories_women_link(self):
        self.footer.click_categories_women_link()

    @unittest.skip("pass")
    def test_click_information_specials_link(self):
        self.footer.click_information_specials_link()

    @unittest.skip("pass")
    def test_click_information_new_products_link(self):
        self.footer.click_information_new_products_link()

    @unittest.skip("pass")
    def test_click_information_best_sellers_link(self):
        self.footer.click_information_best_sellers_link()

    @unittest.skip("pass")
    def test_click_information_our_stores_link(self):
        self.footer.click_information_our_stores_link()

    @unittest.skip("pass")
    def test_click_information_contact_us_link(self):
        self.footer.click_information_contact_us_link()

    @unittest.skip("pass")
    def test_click_information_terms_and_conditions_of_use_link(self):
        self.footer.click_information_terms_and_conditions_of_use_link()

    @unittest.skip("pass")
    def test_click_information_about_us_link(self):
        self.footer.click_information_about_us_link()

    @unittest.skip("pass")
    def test_click_information_sitemap_link(self):
        self.footer.click_information_sitemap_link()

    @unittest.skip("pass")
    def test_click_my_account_my_orders_link(self):
        self.footer.click_my_account_my_orders_link()

    @unittest.skip("pass")
    def test_click_my_account_my_credit_slips_link(self):
        self.footer.click_my_account_my_credit_slips_link()

    @unittest.skip("pass")
    def test_click_my_account_my_addresses_link(self):
        self.footer.click_my_account_my_addresses_link()

    @unittest.skip("pass")
    def test_click_my_account_my_personal_info_link(self):
        self.footer.click_my_account_my_personal_info_link()


if __name__ == '__main__':
    unittest.main()
