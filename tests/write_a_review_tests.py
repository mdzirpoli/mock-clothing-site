"""
Created on February 15, 2020

@author: Mark Zirpoli

This module contains the unit tests for Write A Review Modal
"""

from pages.sign_in_page import SignInPage
from pages.components.modals.write_a_review_modal import WriteAReviewModal
from pages.product_details_page import ProductDetailsPage
from pages.women_page import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class WriteAReviewModalTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.sign_in = SignInPage(self.driver)
        self.sign_in.click_sign_in_menu_button()
        self.sign_in.input_email_address_textbox("test1940@gmail.com")
        self.sign_in.input_password_textbox("abcd1234")
        self.sign_in.click_sign_in_button()
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()
        self.women.click_blouse_thumbnail()
        self.product_details = ProductDetailsPage(self.driver)
        self.write = WriteAReviewModal(self.driver)
        self.write.click_write_a_review_link()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_click_stars_rating(self):
        self.write.click_stars_rating()

    @unittest.skip("pass")
    def test_input_write_a_review_title_textbox(self):
        self.write.input_write_a_review_title_textbox("Here is input")

    @unittest.skip("pass")
    def test_input_write_a_review_comment_textbox(self):
        self.write.input_write_a_review_comment_textbox("Here is a comment")

    @unittest.skip("pass")
    def test_click_write_a_review_send_button(self):
        self.write.click_write_a_review_send_button()

    @unittest.skip("pass")
    def test_click_write_a_review_cancel_button(self):
        self.write.click_write_a_review_cancel_button()

    @unittest.skip("pass")
    def test_click_write_a_review_x_button(self):
        time.sleep(2)
        self.write.click_write_a_review_x_button()


if __name__ == '__main__':
    unittest.main()
