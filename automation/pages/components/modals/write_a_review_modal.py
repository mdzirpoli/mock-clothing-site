"""
Created on February 15, 2020
Modified on December 19, 2020

@author: Mark Zirpoli

This module contains methods for Write A Review Modal
"""

from automation.elements import Button, TextField, Link


class WriteAReviewModal(object):
    """
    Page object for Write A Review Modal
    """
    def __init__(self, driver):
        self.driver = driver

    def click_write_a_review_link(self):
        write_a_review = \
            Link(self.driver,
                 xpath="//*[@id='product_comments_block_extra']/ul/li/a")
        write_a_review.click()

    def click_stars_rating(self):
        stars_rating = Link(self.driver, xpath="//*[@title='4']")
        stars_rating.click()

    def input_write_a_review_title_textbox(self, review):
        write_a_review_title = TextField(self.driver, div_id="comment_title")
        write_a_review_title.input_text(review)

    def input_write_a_review_comment_textbox(self, comment):
        write_a_review_comment = TextField(self.driver, div_id="content")
        write_a_review_comment.input_text(comment)

    def click_write_a_review_send_button(self):
        write_a_review_send = Button(self.driver,
                                     xpath="//*[@id='submitNewMessage']")
        write_a_review_send.click()

    def click_write_a_review_cancel_button(self):
        write_a_review_cancel = \
            Button(self.driver,
                   xpath="//*[@id='new_comment_form_footer']/p[2]/a")
        write_a_review_cancel.click()

    def click_write_a_review_x_button(self):
        write_a_review_x = \
            Button(self.driver,
                   xpath="//*[@id='product']/div[2]/div/div/a")
        write_a_review_x.click()
