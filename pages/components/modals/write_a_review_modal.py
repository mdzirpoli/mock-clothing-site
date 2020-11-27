"""
Created on February 15, 2020

@author: Mark Zirpoli

This module contains methods for Write A Review Modal
"""

from selenium.webdriver.common.by import By


class WriteAReviewModal(object):
    """
    Page object for Write A Review Modal
    """

    # Write A Review Modal locators
    WRITE_A_REVIEW_LINK = (By.XPATH, "//*[@id='product_comments_block_extra']/ul/li/a")
    QUALITY_STARS = (By.XPATH, "//*[@title='4']")
    WRITE_A_REVIEW_TITLE_TEXTBOX = (By.ID, "comment_title")
    WRITE_A_REVIEW_COMMENT_TEXTBOX = (By.ID, "content")
    WRITE_A_REVIEW_SEND_BUTTON = (By.XPATH, "//*[@id='submitNewMessage']")
    WRITE_A_REVIEW_CANCEL_BUTTON = (By.XPATH, "//*[@id='new_comment_form_footer']/p[2]/a")
    WRITE_A_REVIEW_X_BUTTON = (By.XPATH, "//*[@id='product']/div[2]/div/div/a")

    def __init__(self, driver):
        self.driver = driver

    def click_write_a_review_link(self):
        self.driver.find_element(*self.WRITE_A_REVIEW_LINK).click()

    def click_stars_rating(self):
        self.driver.find_element(*self.QUALITY_STARS).click()

    def input_write_a_review_title_textbox(self, review):
        self.driver.find_element(*self.WRITE_A_REVIEW_TITLE_TEXTBOX).send_keys(review)

    def input_write_a_review_comment_textbox(self, comment):
        self.driver.find_element(*self.WRITE_A_REVIEW_COMMENT_TEXTBOX).send_keys(comment)

    def click_write_a_review_send_button(self):
        self.driver.find_element(*self.WRITE_A_REVIEW_SEND_BUTTON).click()

    def click_write_a_review_cancel_button(self):
        self.driver.find_element(*self.WRITE_A_REVIEW_CANCEL_BUTTON).click()

    def click_write_a_review_x_button(self):
        self.driver.find_element(*self.WRITE_A_REVIEW_X_BUTTON).click()
