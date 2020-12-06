"""
Created on January 26, 2020
Modified on December 6, 2020

@author: Mark Zirpoli

This module contains methods for the T-Shirts page
"""

from automation.elements import Button, Link, CheckBox, DropDown
from selenium.webdriver import ActionChains


class TShirtsPage(object):
    """
    Page object for T-Shirts page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_tshirts_nav_menu_button(self):
        tshirts_nav_menu = \
            Button(self.driver, xpath="//*[@id='block_top_menu']/ul/li[3]/a")
        tshirts_nav_menu.click()

    def check_tshirts_size_small_checkbox(self):
        check_tshirts_size_small = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_1")
        check_tshirts_size_small.check()

    def uncheck_tshirts_size_small_checkbox(self):
        uncheck_tshirts_size_small = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_1")
        uncheck_tshirts_size_small.uncheck()

    def check_tshirts_size_medium_checkbox(self):
        check_tshirts_size_medium = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_2")
        check_tshirts_size_medium.check()

    def uncheck_tshirts_size_medium_checkbox(self):
        uncheck_tshirts_size_medium = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_2")
        uncheck_tshirts_size_medium.uncheck()

    def check_tshirts_size_large_checkbox(self):
        check_tshirts_size_large = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_3")
        check_tshirts_size_large.check()

    def uncheck_tshirts_size_large_checkbox(self):
        uncheck_tshirts_size_large = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_3")
        uncheck_tshirts_size_large.uncheck()

    def check_tshirts_color_orange_checkbox(self):
        check_shirts_color_orange = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_13")
        check_shirts_color_orange.check()

    def uncheck_tshirts_color_orange_checkbox(self):
        uncheck_shirts_color_orange = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_13")
        uncheck_shirts_color_orange.uncheck()

    def check_tshirts_color_blue_checkbox(self):
        check_tshirts_color_blue = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_14")
        check_tshirts_color_blue.check()

    def uncheck_tshirts_color_blue_checkbox(self):
        uncheck_tshirts_color_blue = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_14")
        uncheck_tshirts_color_blue.uncheck()

    def check_tshirts_compositions_cotton_checkbox(self):
        check_tshirts_compositions_cotton = \
            CheckBox(self.driver, div_id="layered_id_feature_5")
        check_tshirts_compositions_cotton.check()

    def uncheck_tshirts_compositions_cotton_checkbox(self):
        uncheck_tshirts_compositions_cotton = \
            CheckBox(self.driver, div_id="layered_id_feature_5")
        uncheck_tshirts_compositions_cotton.uncheck()

    def check_tshirts_styles_casual_checkbox(self):
        check_tshirts_styles_casual = \
            CheckBox(self.driver, div_id="layered_id_feature_11")
        check_tshirts_styles_casual.check()

    def uncheck_tshirts_styles_casual_checkbox(self):
        uncheck_tshirts_styles_casual = \
            CheckBox(self.driver, div_id="layered_id_feature_11")
        uncheck_tshirts_styles_casual.uncheck()

    def check_tshirts_properties_short_sleeve_checkbox(self):
        check_tshirts_properties_short_sleeve = \
            CheckBox(self.driver, div_id="layered_id_feature_17")
        check_tshirts_properties_short_sleeve.check()

    def uncheck_tshirts_properties_short_sleeve_checkbox(self):
        uncheck_tshirts_properties_short_sleeve = \
            CheckBox(self.driver, div_id="layered_id_feature_17")
        uncheck_tshirts_properties_short_sleeve.uncheck()

    def check_tshirts_availability_in_stock_checkbox(self):
        check_tshirts_availability_in_stock = \
            CheckBox(self.driver, div_id="layered_quantity_1")
        check_tshirts_availability_in_stock.check()

    def uncheck_tshirts_availability_in_stock_checkbox(self):
        uncheck_tshirts_availability_in_stock = \
            CheckBox(self.driver, div_id="layered_quantity_1")
        uncheck_tshirts_availability_in_stock.uncheck()

    def check_tshirts_manufacturer_fashion_manufacturer_checkbox(self):
        check_tshirts_manufacturer_fashion = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        check_tshirts_manufacturer_fashion.check()

    def uncheck_tshirts_manufacturer_fashion_manufacturer_checkbox(self):
        uncheck_tshirts_manufacturer_fashion = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        uncheck_tshirts_manufacturer_fashion.uncheck()

    def check_tshirts_condition_new_checkbox(self):
        check_tshirts_condition_new = \
            CheckBox(self.driver, div_id="layered_condition_new")
        check_tshirts_condition_new.check()

    def uncheck_tshirts_condition_new_checkbox(self):
        uncheck_tshirts_condition_new = \
            CheckBox(self.driver, div_id="layered_condition_new")
        uncheck_tshirts_condition_new.uncheck()

    def click_tshirts_information_delivery_link(self):
        tshirts_information_delivery = \
            Link(self.driver, xpath="//*[@title='Delivery']")
        tshirts_information_delivery.click()

    def click_tshirts_legal_notice_link(self):
        tshirts_legal_notice = \
            Link(self.driver, xpath="//*[@title='Legal Notice']")
        tshirts_legal_notice.click()

    def click_tshirts_terms_and_condition_of_use_link(self):
        tshirts_terms_and_conditions_of_use = \
            Link(self.driver,
                 xpath="//*[@title='Terms and conditions of use']")
        tshirts_terms_and_conditions_of_use.click()

    def click_tshirts_about_us_link(self):
        tshirts_about_us = Link(self.driver, xpath="//*[@title='About us']")
        tshirts_about_us.click()

    def click_tshirts_secure_payment_link(self):
        tshirts_secure_payment = \
            Link(self.driver, xpath="//*[@title='Secure payment']")
        tshirts_secure_payment.click()

    def click_tshirts_our_stores_link(self):
        tshirts_our_stores = \
            Link(self.driver, xpath="//*[@title='Our stores']")
        tshirts_our_stores.click()

    def click_tshirts_all_specials_button(self):
        tshirts_all_specials = \
            Button(self.driver, xpath="//span[text()='All specials']")
        tshirts_all_specials.click()

    def click_tshirts_discover_our_stores_button(self):
        tshirts_discover_our_stores = \
            Button(self.driver, xpath="//span[text()='Discover our stores']")
        tshirts_discover_our_stores.click()

    def select_tshirts_sort_by_dropdown(self, value):
        tshirts_sort_by = DropDown(self.driver, div_id="selectProductSort")
        tshirts_sort_by.select_dropdown(value)

    def click_tshirts_view_grid_button(self):
        tshirts_view_grid = Button(self.driver, xpath="//*[@id='grid']/a/i")
        tshirts_view_grid.click()

    def click_tshirts_list_grid_button(self):
        tshirts_list_grid = Button(self.driver, xpath="//*[@id='list']/a/i")
        tshirts_list_grid.click()

    def click_faded_short_sleeve_tshirts_thumbnail(self):
        faded_short_sleeve_tshirts = \
            Link(self.driver,
                 xpath="//*[@title='Faded Short Sleeve T-shirts'][1]")
        faded_short_sleeve_tshirts.click()

    def click_printed_chiffon_dress_quick_view_button(self):
        button = \
            self.driver.find_element_by_xpath("//span[text()='Quick view']")
        thumbnail = \
            self.driver.\
            find_element_by_xpath("//*[@title='Faded Short Sleeve T-shirts'][1]")
        hover = \
            ActionChains(self.driver).move_to_element(button).\
            move_to_element(thumbnail)
        hover.click().perform()
