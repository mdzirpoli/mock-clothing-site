"""
Created on November 24, 2019

@author: Mark Zirpoli

This module contains the unit tests for the Contact Us page
"""

from pages.contact_us_page import ContactUsPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class ContactUsPageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.contact_us = ContactUsPage(self.driver)
        self.contact_us.click_contact_us_menu_button()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_select_subject_heading_dropdown(self):
        self.contact_us.click_subject_heading_dropdown("Webmaster")

    @unittest.skip("pass")
    def test_input_contact_us_email_address_textbox(self):
        self.contact_us.input_contact_us_email_address_textbox("email@email.com")

    @unittest.skip("pass")
    def test_input_order_reference_textbox(self):
        self.contact_us.input_order_reference_textbox("432190")

    @unittest.skip("pass")
    def test_attach_file_upload(self):
        self.contact_us.attach_file_upload("/Users/mark/Desktop/Programming/test.pdf")

    @unittest.skip("pass")
    def test_input_contact_us_message_textbox(self):
        self.contact_us.input_contact_us_message_textbox("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    @unittest.skip("pass")
    def test_click_contact_us_send_button(self):
        self.contact_us.click_contact_us_send_button()


if __name__ == '__main__':
    unittest.main()
