"""
Created on January 20, 2020
Modified on December 27, 2020

@author: Mark Zirpoli

This module contains methods for the Dresses page
"""

from automation.elements import Button, DropDown, Link, CheckBox
from selenium.webdriver import ActionChains


class DressesPage(object):
    """
    Page object for Dresses page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_dresses_nav_menu_button(self):
        dresses_nav_menu = \
            Button(self.driver,
                   xpath="//*[@id='block_top_menu']/ul/li[2]/a")
        dresses_nav_menu.click()

    def click_dresses_casual_dresses_link(self):
        dresses_casual_dresses = \
            Link(self.driver,
                 xpath="//*[@id='categories_block_left']/div/ul/li[1]/a")
        dresses_casual_dresses.click()

    def click_dresses_evening_dresses_link(self):
        dresses_evening_dresses = \
            Link(self.driver,
                 xpath="//*[@id='categories_block_left']/div/ul/li[2]/a")
        dresses_evening_dresses.click()

    def click_dresses_summer_dresses_link(self):
        dresses_summer_dresses = \
            Link(self.driver,
                 xpath="//*[@id='categories_block_left']/div/ul/li[3]/a")
        dresses_summer_dresses.click()

    def check_categories_casual_dresses_checkbox(self):
        categories_casual_dresses = \
            CheckBox(self.driver, div_id="layered_category_9")
        categories_casual_dresses.check()

    def uncheck_categories_casual_dresses_checkbox(self):
        uncheck_categories_casual_dresses = \
            CheckBox(self.driver, div_id="layered_category_9")
        uncheck_categories_casual_dresses.uncheck()

    def check_categories_evening_dresses_checkbox(self):
        categories_evening_dresses = CheckBox(self.driver,
                                              div_id="layered_category_10")
        categories_evening_dresses.check()

    def uncheck_categories_evening_dresses_checkbox(self):
        uncheck_categories_evening_dresses = \
            CheckBox(self.driver, div_id="layered_category_10")
        uncheck_categories_evening_dresses.uncheck()

    def check_categories_summer_dresses_checkbox(self):
        categories_summer_dresses = \
            CheckBox(self.driver, div_id="layered_category_11")
        categories_summer_dresses.check()

    def uncheck_categories_summer_dresses_checkbox(self):
        uncheck_categories_summer_dresses = \
            CheckBox(self.driver, div_id="layered_category_11")
        uncheck_categories_summer_dresses.uncheck()

    def check_dresses_size_small_checkbox(self):
        dresses_size_small = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_1")
        dresses_size_small.check()

    def uncheck_dresses_size_small_checkbox(self):
        uncheck_dresses_size_small = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_1")
        uncheck_dresses_size_small.uncheck()

    def check_dresses_size_medium_checkbox(self):
        dresses_size_medium = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_2")
        dresses_size_medium.check()

    def uncheck_dresses_size_medium_checkbox(self):
        uncheck_dresses_size_medium = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_2")
        uncheck_dresses_size_medium.uncheck()

    def check_dresses_size_large_checkbox(self):
        dresses_size_large = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_3")
        dresses_size_large.check()

    def uncheck_dresses_size_large_checkbox(self):
        uncheck_dresses_size_large = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_3")
        uncheck_dresses_size_large.uncheck()

    def check_dresses_color_beige_checkbox(self):
        dresses_color_beige = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_7")
        dresses_color_beige.check()

    def uncheck_dresses_color_beige_checkbox(self):
        uncheck_dresses_color_beige = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_7")
        uncheck_dresses_color_beige.uncheck()

    def check_dresses_color_white_checkbox(self):
        dresses_color_white = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_8")
        dresses_color_white.check()

    def uncheck_dresses_color_white_checkbox(self):
        uncheck_dresses_color_white = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_8")
        uncheck_dresses_color_white.uncheck()

    def check_dresses_color_black_checkbox(self):
        dresses_color_black = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_11")
        dresses_color_black.check()

    def uncheck_dresses_color_black_checkbox(self):
        uncheck_dresses_color_black = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_11")
        uncheck_dresses_color_black.uncheck()

    def check_dresses_color_orange_checkbox(self):
        dresses_color_orange = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_13")
        dresses_color_orange.check()

    def uncheck_dresses_color_orange_checkbox(self):
        uncheck_dresses_color_orange = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_13")
        uncheck_dresses_color_orange.uncheck()

    def check_dresses_color_blue_checkbox(self):
        dresses_color_blue = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_14")
        dresses_color_blue.check()

    def uncheck_dresses_color_blue_checkbox(self):
        uncheck_dresses_color_blue = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_14")
        uncheck_dresses_color_blue.uncheck()

    def check_dresses_color_green_checkbox(self):
        dresses_color_green = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_15")
        dresses_color_green.check()

    def uncheck_dresses_color_green_checkbox(self):
        uncheck_dresses_color_green = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_15")
        uncheck_dresses_color_green.uncheck()

    def check_dresses_color_yellow_checkbox(self):
        dresses_color_yellow = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_16")
        dresses_color_yellow.check()

    def uncheck_dresses_color_yellow_checkbox(self):
        uncheck_dresses_color_yellow = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_16")
        uncheck_dresses_color_yellow.uncheck()

    def check_dresses_color_pink_checkbox(self):
        dresses_color_pink = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_24")
        dresses_color_pink.check()

    def uncheck_dresses_color_pink_checkbox(self):
        uncheck_dresses_color_pink = \
            CheckBox(self.driver, div_id="layered_id_attribute_group_24")
        uncheck_dresses_color_pink.uncheck()

    def check_dresses_compositions_cotton_checkbox(self):
        dresses_compositions_cotton = \
            CheckBox(self.driver, div_id="layered_id_feature_5")
        dresses_compositions_cotton.check()

    def uncheck_dresses_compositions_cotton_checkbox(self):
        uncheck_dresses_compositions_cotton = \
            CheckBox(self.driver, div_id="layered_id_feature_5")
        uncheck_dresses_compositions_cotton.uncheck()

    def check_dresses_compositions_polyester_checkbox(self):
        dresses_compositions_polyester = \
            CheckBox(self.driver, div_id="layered_id_feature_1")
        dresses_compositions_polyester.check()

    def uncheck_dresses_compositions_polyester_checkbox(self):
        uncheck_dresses_compositions_polyester = \
            CheckBox(self.driver, div_id="layered_id_feature_1")
        uncheck_dresses_compositions_polyester.uncheck()

    def check_dresses_compositions_viscose_checkbox(self):
        dresses_compositions_viscose = \
            CheckBox(self.driver, div_id="layered_id_feature_3")
        dresses_compositions_viscose.check()

    def uncheck_dresses_compositions_viscose_checkbox(self):
        uncheck_dresses_compositions_viscose = \
            CheckBox(self.driver, div_id="layered_id_feature_3")
        uncheck_dresses_compositions_viscose.uncheck()

    def check_dresses_styles_casual_checkbox(self):
        dresses_styles_casual = \
            CheckBox(self.driver, div_id="layered_id_feature_11")
        dresses_styles_casual.check()

    def uncheck_dresses_styles_casual_checkbox(self):
        uncheck_dresses_styles_casual = \
            CheckBox(self.driver, div_id="layered_id_feature_11")
        uncheck_dresses_styles_casual.uncheck()

    def check_dresses_styles_dressy_checkbox(self):
        dresses_styles_dressy = \
            CheckBox(self.driver, div_id="layered_id_feature_16")
        dresses_styles_dressy.check()

    def uncheck_dresses_styles_dressy_checkbox(self):
        uncheck_dresses_styles_dressy = \
            CheckBox(self.driver, div_id="layered_id_feature_16")
        uncheck_dresses_styles_dressy.uncheck()

    def check_dresses_styles_girly_checkbox(self):
        dresses_styles_girly = \
            CheckBox(self.driver, div_id="layered_id_feature_13")
        dresses_styles_girly.check()

    def uncheck_dresses_styles_girly_checkbox(self):
        uncheck_dresses_styles_girly = \
            CheckBox(self.driver, div_id="layered_id_feature_13")
        uncheck_dresses_styles_girly.uncheck()

    def check_dresses_properties_colorful_dress_checkbox(self):
        dresses_properties_colorful_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_18")
        dresses_properties_colorful_dress.check()

    def uncheck_dresses_properties_colorful_dress_checkbox(self):
        uncheck_dresses_properties_colorful_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_18")
        uncheck_dresses_properties_colorful_dress.uncheck()

    def check_dresses_properties_maxi_dress_checkbox(self):
        dresses_properties_maxi_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_21")
        dresses_properties_maxi_dress.check()

    def uncheck_dresses_properties_maxi_dress_checkbox(self):
        uncheck_dresses_properties_maxi_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_21")
        uncheck_dresses_properties_maxi_dress.uncheck()

    def check_dresses_properties_midi_dress_checkbox(self):
        dresses_properties_midi_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_20")
        dresses_properties_midi_dress.check()

    def uncheck_dresses_properties_midi_dress_checkbox(self):
        uncheck_dresses_properties_midi_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_20")
        uncheck_dresses_properties_midi_dress.uncheck()

    def check_dresses_properties_short_dress_checkbox(self):
        dresses_properties_short_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_19")
        dresses_properties_short_dress.check()

    def uncheck_dresses_properties_short_dress_checkbox(self):
        uncheck_dresses_properties_short_dress = \
            CheckBox(self.driver, div_id="layered_id_feature_19")
        uncheck_dresses_properties_short_dress.uncheck()

    def check_dresses_availability_in_stock_checkbox(self):
        dresses_availability_in_stock = \
            CheckBox(self.driver, div_id="layered_quantity_1")
        dresses_availability_in_stock.check()

    def uncheck_dresses_availability_in_stock_checkbox(self):
        uncheck_dresses_availability_in_stock = \
            CheckBox(self.driver, div_id="layered_quantity_1")
        uncheck_dresses_availability_in_stock.uncheck()

    def check_dresses_manufacturer_fashion_manufacturer_checkbox(self):
        dresses_manufacturer_fashion_manufacturer = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        dresses_manufacturer_fashion_manufacturer.check()

    def uncheck_dresses_manufacturer_fashion_manufacturer_checkbox(self):
        uncheck_dresses_manufacturer_fashion_manufacturer = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        uncheck_dresses_manufacturer_fashion_manufacturer.uncheck()

    def check_dresses_condition_new_checkbox(self):
        dresses_condition_new = \
            CheckBox(self.driver, div_id="layered_condition_new")
        dresses_condition_new.check()

    def uncheck_dresses_condition_new_checkbox(self):
        uncheck_dresses_condition_new = \
            CheckBox(self.driver, div_id="layered_condition_new")
        uncheck_dresses_condition_new.uncheck()

    def click_dresses_information_delivery_link(self):
        dresses_information_delivery = \
            Link(self.driver, xpath="//*[@title='Delivery']")
        dresses_information_delivery.click()

    def click_dresses_information_legal_notice_link(self):
        dresses_information_legal_notice = \
            Link(self.driver, xpath="//*[@title='Legal Notice']")
        dresses_information_legal_notice.click()

    def click_dresses_information_terms_and_conditions_of_use_link(self):
        dresses_information_terms_and_conditions_of_use = \
            Link(self.driver,
                 xpath="//*[@title='Terms and conditions of use']")
        dresses_information_terms_and_conditions_of_use.click()

    def click_dresses_information_about_us_link(self):
        dresses_information_about_us = \
            Link(self.driver, xpath="//*[@title='About us']")
        dresses_information_about_us.click()

    def click_dresses_information_secure_payment_link(self):
        dresses_information_secure_payment = \
            Link(self.driver, xpath="//*[@title='Secure payment']")
        dresses_information_secure_payment.click()

    def click_dresses_information_our_stores_link(self):
        dresses_information_our_stores = \
            Link(self.driver, xpath="//*[@title='Our stores']")
        dresses_information_our_stores.click()

    def click_dresses_all_specials_button(self):
        dresses_all_specials = \
            Button(self.driver, xpath="//span[text()='All specials']")
        dresses_all_specials.click()

    def click_dresses_discover_our_stores_button(self):
        dresses_discover_our_stores = \
            Button(self.driver,
                   xpath="//span[text()='Discover our stores']")
        dresses_discover_our_stores.click()

    def click_subcategories_casual_dresses_thumbnail(self):
        subcategories_casual_dresses = \
            Link(self.driver,
                 xpath="//*[@id='subcategories']/ul/li[1]/div[1]/a/img")
        subcategories_casual_dresses.click()

    def click_subcategories_evening_dresses_thumbnail(self):
        subcategories_evening_dresses = \
            Link(self.driver,
                 xpath="//*[@id='subcategories']/ul/li[2]/div[1]/a/img")
        subcategories_evening_dresses.click()

    def click_subcategories_summer_dresses_thumbnail(self):
        subcategories_summer_dresses = \
            Link(self.driver,
                 xpath="//*[@id='subcategories']/ul/li[3]/div[1]/a/img")
        subcategories_summer_dresses.click()

    def select_dresses_sort_by_dropdown(self, value):
        dresses_sort_by = DropDown(self.driver, div_id="selectProductSort")
        dresses_sort_by.select_dropdown(value)

    def click_dresses_view_grid_button(self):
        dresses_view_grid = Button(self.driver, xpath="//*[@id='grid']/a/i")
        dresses_view_grid.click()

    def click_dresses_list_grid_button(self):
        dresses_list_grid = Button(self.driver, xpath="//*[@id='list']/a/i")
        dresses_list_grid.click()

    def click_printed_chiffon_dress_thumbnail(self):
        printed_chiffon_dress = \
            Link(self.driver, xpath="//*[@title='Printed Chiffon Dress'][1]")
        printed_chiffon_dress.click()

    def click_printed_chiffon_dress_quick_view_button(self):
        button = self.driver. \
            find_element_by_xpath("//span[text()='Quick view']")
        thumbnail = self.\
            driver.\
            find_element_by_xpath("//*[@title='Printed Chiffon Dress'][1]")
        hover = ActionChains(self.driver)\
            .move_to_element(button).move_to_element(thumbnail)
        hover.click().perform()
