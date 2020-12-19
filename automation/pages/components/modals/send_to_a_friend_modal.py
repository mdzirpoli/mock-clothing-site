"""
Created on February 15, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for the Send To A Friend modal
"""

from automation.elements import Button, TextField, Link


class SendToAFriendModal(object):
    """
    Page object for Send To A Friend Modal
    """
    def __init__(self, driver):
        self.driver = driver

    def click_send_to_a_friend_link(self):
        send_to_a_friend = Link(self.driver, div_id="send_friend_button")
        send_to_a_friend.click()

    def input_name_of_your_friend_textbox(self, friend):
        name_of_your_friend = TextField(self.driver, div_id="friend_name")
        name_of_your_friend.input_text(friend)

    def input_email_address_of_your_friend_textbox(self, email):
        email_address_of_your_friend = TextField(self.driver,
                                                 div_id="friend_email")
        email_address_of_your_friend.input_text(email)

    def click_send_to_a_friend_send_button(self):
        send_to_a_friend_send = Button(self.driver, div_id="sendEmail")
        send_to_a_friend_send.click()

    def click_send_to_a_friend_cancel_button(self):
        send_to_a_friend_cancel = \
            Button(self.driver,
                   xpath="//*[@id='send_friend_form_content']/p/a")
        send_to_a_friend_cancel.click()

    def click_send_to_a_friend_x_button(self):
        send_to_a_friend_x = Button(self.driver,
                                    xpath="//*[@title='Close']")
        send_to_a_friend_x.click()
