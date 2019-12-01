"""
Created on November 24, 2019

@author: Mark Zirpoli
"""


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
