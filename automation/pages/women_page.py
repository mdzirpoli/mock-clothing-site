"""
Created on December 1, 2019
Modified on December 21, 2020

@author: Mark Zirpoli

This module contains methods for the Women page
"""

from automation.elements import Button, Link, CheckBox, DropDown
from selenium.webdriver import ActionChains


class WomenPage(object):
    """
    Page object for Women page
    """
    def __init__(self, driver):
        self.driver = driver

    def click_women_nav_menu_button(self):
        women_nav_menu = \
            Button(self.driver, xpath="//*[@id='block_top_menu']/ul/li[1]/a")
        women_nav_menu.click()

    def click_women_tops_link(self):
        women_tops = \
            Link(self.driver,
                 xpath="//*[@id='categories_block_left']/div/ul/li[1]/a")
        women_tops.click()

    def click_women_dresses_link(self):
        women_addresses = \
            Link(self.driver,
                 xpath="//*[@id='categories_block_left']/div/ul/li[2]/a")
        women_addresses.click()

    def check_categories_tops_checkbox(self):
        categories_tops = CheckBox(self.driver, div_id="layered_category_4")
        categories_tops.check()

    def uncheck_categories_tops_checkbox(self):
        categories_tops = CheckBox(self.driver, div_id="layered_category_4")
        categories_tops.uncheck()

    def check_categories_dresses_checkbox(self):
        categories_dresses = CheckBox(self.driver, div_id="layered_category_8")
        categories_dresses.check()

    def uncheck_categories_dresses_checkbox(self):
        categories_dresses = CheckBox(self.driver, div_id="layered_category_8")
        categories_dresses.uncheck()

    def check_size_small_checkbox(self):
        size_small = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_1")
        size_small.check()

    def uncheck_size_small_checkbox(self):
        size_small = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_1")
        size_small.uncheck()

    def check_size_medium_checkbox(self):
        size_medium = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_2")
        size_medium.check()

    def uncheck_size_medium_checkbox(self):
        size_medium = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_2")
        size_medium.uncheck()

    def check_size_large_checkbox(self):
        size_large = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_3")
        size_large.check()

    def uncheck_size_large_checkbox(self):
        size_large = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_3")
        size_large.uncheck()

    def check_color_beige_checkbox(self):
        color_beige = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_7")
        color_beige.check()

    def uncheck_color_beige_checkbox(self):
        color_beige = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_7")
        color_beige.uncheck()

    def check_color_white_checkbox(self):
        color_white = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_8")
        color_white.check()

    def uncheck_color_white_checkbox(self):
        color_white = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_8")
        color_white.uncheck()

    def check_color_black_checkbox(self):
        color_black = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_11")
        color_black.check()

    def uncheck_color_black_checkbox(self):
        color_black = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_11")
        color_black.uncheck()

    def check_color_orange_checkbox(self):
        color_orange = CheckBox(self.driver,
                                div_id="layered_id_attribute_group_13")
        color_orange.check()

    def uncheck_color_orange_checkbox(self):
        color_orange = CheckBox(self.driver,
                                div_id="layered_id_attribute_group_13")
        color_orange.uncheck()

    def check_color_blue_checkbox(self):
        color_blue = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_14")
        color_blue.check()

    def uncheck_color_blue_checkbox(self):
        color_blue = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_14")
        color_blue.uncheck()

    def check_color_green_checkbox(self):
        color_green = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_15")
        color_green.check()

    def uncheck_color_green_checkbox(self):
        color_green = CheckBox(self.driver,
                               div_id="layered_id_attribute_group_15")
        color_green.uncheck()

    def check_color_yellow_checkbox(self):
        color_yellow = CheckBox(self.driver,
                                div_id="layered_id_attribute_group_16")
        color_yellow.check()

    def uncheck_color_yellow_checkbox(self):
        color_yellow = CheckBox(self.driver,
                                div_id="layered_id_attribute_group_16")
        color_yellow.uncheck()

    def check_color_pink_checkbox(self):
        color_pink = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_24")
        color_pink.check()

    def uncheck_color_pink_checkbox(self):
        color_pink = CheckBox(self.driver,
                              div_id="layered_id_attribute_group_24")
        color_pink.uncheck()

    def check_compositions_cotton_checkbox(self):
        compositions_cotton = CheckBox(self.driver,
                                       div_id="layered_id_feature_5")
        compositions_cotton.check()

    def uncheck_compositions_cotton_checkbox(self):
        compositions_cotton = CheckBox(self.driver,
                                       div_id="layered_id_feature_5")
        compositions_cotton.uncheck()

    def check_compositions_polyester_checkbox(self):
        compositions_polyester = CheckBox(self.driver,
                                          div_id="layered_id_feature_1")
        compositions_polyester.check()

    def uncheck_compositions_polyester_checkbox(self):
        compositions_polyester = CheckBox(self.driver,
                                          div_id="layered_id_feature_1")
        compositions_polyester.uncheck()

    def check_compositions_viscose_checkbox(self):
        compositions_viscose = CheckBox(self.driver,
                                        div_id="layered_id_feature_3")
        compositions_viscose.check()

    def uncheck_compositions_viscose_checkbox(self):
        compositions_viscose = CheckBox(self.driver,
                                        div_id="layered_id_feature_3")
        compositions_viscose.uncheck()

    def check_styles_casual_checkbox(self):
        styles_casual = CheckBox(self.driver, div_id="layered_id_feature_11")
        styles_casual.check()

    def uncheck_styles_casual_checkbox(self):
        styles_casual = CheckBox(self.driver, div_id="layered_id_feature_11")
        styles_casual.uncheck()

    def check_styles_dressy_checkbox(self):
        styles_dressy = CheckBox(self.driver, div_id="layered_id_feature_16")
        styles_dressy.check()

    def uncheck_styles_dressy_checkbox(self):
        styles_dressy = CheckBox(self.driver, div_id="layered_id_feature_16")
        styles_dressy.uncheck()

    def check_styles_girly_checkbox(self):
        styles_girly = CheckBox(self.driver, div_id="layered_id_feature_13")
        styles_girly.check()

    def uncheck_styles_girly_checkbox(self):
        styles_girly = CheckBox(self.driver, div_id="layered_id_feature_13")
        styles_girly.uncheck()

    def check_properties_colorful_dress_checkbox(self):
        properties_colorful_dress = CheckBox(self.driver,
                                             div_id="layered_id_feature_18")
        properties_colorful_dress.check()

    def uncheck_properties_colorful_dress_checkbox(self):
        properties_colorful_dress = CheckBox(self.driver,
                                             div_id="layered_id_feature_18")
        properties_colorful_dress.uncheck()

    def check_properties_maxi_dress_checkbox(self):
        properties_maxi_dress = CheckBox(self.driver,
                                         div_id="layered_id_feature_21")
        properties_maxi_dress.check()

    def uncheck_properties_maxi_dress_checkbox(self):
        properties_maxi_dress = CheckBox(self.driver,
                                         div_id="layered_id_feature_21")
        properties_maxi_dress.uncheck()

    def check_properties_midi_dress_checkbox(self):
        properties_midi_dress = CheckBox(self.driver,
                                         div_id="layered_id_feature_20")
        properties_midi_dress.check()

    def uncheck_properties_midi_dress_checkbox(self):
        properties_midi_dress = CheckBox(self.driver,
                                         div_id="layered_id_feature_20")
        properties_midi_dress.uncheck()

    def check_properties_short_dress_checkbox(self):
        properties_short_dress = CheckBox(self.driver,
                                          div_id="layered_id_feature_19")
        properties_short_dress.check()

    def uncheck_properties_short_dress_checkbox(self):
        properties_short_dress = CheckBox(self.driver,
                                          div_id="layered_id_feature_19")
        properties_short_dress.uncheck()

    def check_properties_short_sleeve_checkbox(self):
        properties_short_sleeve = CheckBox(self.driver,
                                           div_id="layered_id_feature_17")
        properties_short_sleeve.check()

    def uncheck_properties_short_sleeve_checkbox(self):
        properties_short_sleeve = CheckBox(self.driver,
                                           div_id="layered_id_feature_17")
        properties_short_sleeve.uncheck()

    def check_availability_in_stock_checkbox(self):
        availability_in_stock = CheckBox(self.driver,
                                         div_id="layered_quantity_1")
        availability_in_stock.check()

    def uncheck_availability_in_stock_checkbox(self):
        availability_in_stock = CheckBox(self.driver,
                                         div_id="layered_quantity_1")
        availability_in_stock.uncheck()

    def check_manufacturer_fashion_manufacturer_checkbox(self):
        manufacturer_fashion_manufacturer = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        manufacturer_fashion_manufacturer.check()

    def uncheck_manufacturer_fashion_manufacturer_checkbox(self):
        manufacturer_fashion_manufacturer = \
            CheckBox(self.driver, div_id="layered_manufacturer_1")
        manufacturer_fashion_manufacturer.uncheck()

    def check_condition_new_checkbox(self):
        condition_new = CheckBox(self.driver,
                                 div_id="layered_condition_new")
        condition_new.check()

    def uncheck_condition_new_checkbox(self):
        condition_new = CheckBox(self.driver,
                                 div_id="layered_condition_new")
        condition_new.uncheck()

    def click_information_delivery_link(self):
        information_delivery = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[1]/a")
        information_delivery.click()

    def click_information_legal_notice_link(self):
        information_legal_notice = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[2]/a")
        information_legal_notice.click()

    def click_information_terms_and_conditions_of_use_link(self):
        information_terms_and_conditions_of_use = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[3]/a")
        information_terms_and_conditions_of_use.click()

    def click_information_about_us_link(self):
        information_about_us = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[4]/a")
        information_about_us.click()

    def click_information_secure_payment_link(self):
        information_secure_payment = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[5]/a")
        information_secure_payment.click()

    def click_information_our_stores_link(self):
        information_our_stores = \
            Link(self.driver,
                 xpath="//*[@id='informations_block_left_1']/div/ul/li[6]/a")
        information_our_stores.click()

    def click_women_all_specials_button(self):
        women_all_specials = Button(self.driver,
                                    xpath="//span[text()='All specials']")
        women_all_specials.click()

    def click_women_discover_our_stores_button(self):
        women_discover_our_stores = \
            Button(self.driver, xpath="//span[text()='Discover our stores']")
        women_discover_our_stores.click()

    def select_subcategories_tops_thumbnail(self):
        subcategories_tops = \
            Button(self.driver,
                   xpath="/html/body/div/div[2]/div/div[3]/div[2]/div[2]/ul/li[1]/div[1]/a/img")
        subcategories_tops.click()

    def select_subcategories_dresses_thumbnail(self):
        subcategories_dresses = \
            Button(self.driver,
                   xpath="//*[@id='subcategories']/ul/li[2]/div[1]/a/img")
        subcategories_dresses.click()

    def select_sort_by_dropdown(self, value):
        sort_by = DropDown(self.driver, div_id="selectProductSort")
        sort_by.select_dropdown(value)

    def click_view_grid_button(self):
        view_grid = Button(self.driver, xpath="//*[@id='grid']/a/i")
        view_grid.click()

    def click_list_grid_button(self):
        list_grid = Button(self.driver, xpath="//*[@id='list']/a/i")
        list_grid.click()

    def click_blouse_thumbnail(self):
        blouse = \
            Button(self.driver,
                   xpath="//*[@id='center_column']/ul/li[2]/div/div[2]/h5/a")
        blouse.click()

    def click_blouse_hover_quick_view_button(self):
        button = self.driver.\
            find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[1]/div/a[2]")
        product = self.driver.find_element_by_xpath("//*[@title='Blouse']")
        ActionChains(self.driver).move_to_element(product).click(button).perform()

    def click_blouse_hover_add_to_cart_button(self):
        button = self.driver.\
            find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a[1]")
        product = self.driver.find_element_by_xpath("//*[@title='Blouse']")
        ActionChains(self.driver).move_to_element(product).click(button).perform()

    def click_blouse_hover_more_button(self):
        button = self.driver.\
            find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a[2]/span")
        product = self.driver.find_element_by_xpath("//*[@title='Blouse']")
        ActionChains(self.driver).move_to_element(product).click(button).perform()

    def click_blouse_hover_add_to_wishlist_button(self):
        button = self.driver.\
            find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[3]/div[1]/a")
        product = self.driver.find_element_by_xpath("//*[@title='Blouse']")
        ActionChains(self.driver).move_to_element(product).click(button).perform()

    def click_blouse_hover_add_to_compare_button(self):
        button = self.driver.\
            find_element_by_xpath("//*[@id='center_column']/ul/li[2]/div/div[3]/div[1]/a")
        product = self.driver.find_element_by_xpath("//*[@title='Blouse']")
        ActionChains(self.driver).move_to_element(product).click(button).perform()
