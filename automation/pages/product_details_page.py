"""
Created on November 8, 2020
Modified on December 13, 2020

@author: Mark Zirpoli

This module contains methods for the Women Blouse Product Details page
"""

from automation.elements import Button, Link, TextField, DropDown


class ProductDetailsPage(object):
    """
    Page object for the Women Blouse Product Details page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_product_details_page_tweet_button(self):
        product_details_page_tweet = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/div/div/div[3]/p[7]/button[1]")
        product_details_page_tweet.click()

    def click_product_details_page_facebook_button(self):
        product_details_page_facebook = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/div/div/div[3]/p[7]/button[2]")
        product_details_page_facebook.click()

    def click_product_details_page_google_plus_button(self):
        product_details_page_google_plus = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/div/div/div[3]/p[7]/button[3]")
        product_details_page_google_plus.click()

    def click_product_details_page_pinterest_button(self):
        product_details_page_pinterest = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/div/div/div[3]/p[7]/button[4]")
        product_details_page_pinterest.click()

    def click_send_to_a_friend_link(self):
        send_to_friend = Link(self.driver, div_id="send_friend_button")
        send_to_friend.click()

    def click_product_details_page_print_link(self):
        product_details_page_print = \
            Link(self.driver, xpath="//*[@id='usefull_link_block']/li[2]/a")
        product_details_page_print.click()

    def input_quantity_textbox(self, quantity):
        input_quantity = TextField(self.driver, div_id="quantity_wanted")
        input_quantity.input_text(quantity)

    def click_quantity_minus_button(self):
        quantity_minus = \
            Button(self.driver,
                   xpath="//*[@id='quantity_wanted_p']/a[1]/span/i")
        quantity_minus.click()

    def click_quantity_plus_button(self):
        quantity_plus = \
            Button(self.driver,
                   xpath="//*[@id='quantity_wanted_p']/a[2]/span/i")
        quantity_plus.click()

    def select_product_details_page_size_dropdown(self, size):
        product_details_page_size = DropDown(self.driver, div_id="group_1")
        product_details_page_size.select_dropdown(size)

    def click_product_details_page_color_white_button(self):
        product_details_color_white = Button(self.driver, div_id="color_8")
        product_details_color_white.click()

    def click_product_details_page_color_black_button(self):
        product_details_page_color_black = Button(self.driver,
                                                  div_id="color_11")
        product_details_page_color_black.click()

    def click_product_details_page_add_to_cart_button(self):
        product_details_page_add_to_cart = Button(self.driver,
                                                  div_name="Submit")
        product_details_page_add_to_cart.click()

    def click_product_details_page_add_to_wishlist_button(self):
        product_details_page_add_to_wishlist = Button(self.driver,
                                                      div_id="wishlist_button")
        product_details_page_add_to_wishlist.click()
