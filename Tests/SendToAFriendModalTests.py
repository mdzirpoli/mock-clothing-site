"""
Created on February 15, 2020

@author: Mark Zirpoli

This module contains the unit tests for the Send To A Friend Modal
"""

from Pages.Components.Modals.SendToAFriendModal import SendToAFriendModal
from Pages.ProductDetailsPage import ProductDetailsPage
from Pages.WomenPage import WomenPage
from selenium import webdriver
import unittest
import time

url = "http://automationpractice.com/index.php"


class SendToAFriendModalTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.women = WomenPage(self.driver)
        self.women.click_women_nav_menu_button()
        self.women.click_blouse_thumbnail()
        self.product_details = ProductDetailsPage(self.driver)
        self.modal = SendToAFriendModal(self.driver)
        self.modal.click_send_to_a_friend_link()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()

    @unittest.skip("pass")
    def test_input_name_of_your_friend_textbox(self):
        self.modal.input_name_of_your_friend_textbox("Amy Smith")

    @unittest.skip("pass")
    def test_input_email_address_of_your_friend_textbox(self):
        self.modal.input_email_address_of_your_friend_textbox("amysmith@email.com")

    @unittest.skip("pass")
    def test_click_send_to_a_friend_send_button(self):
        self.modal.click_send_to_a_friend_send_button()

    @unittest.skip("pass")
    def test_click_send_to_a_friend_cancel_button(self):
        self.modal.click_send_to_a_friend_cancel_button()

    @unittest.skip("pass")
    def test_click_send_to_a_friend_x_button(self):
        time.sleep(2)
        self.modal.click_send_to_a_friend_x_button()


if __name__ == '__main__':
    unittest.main()
