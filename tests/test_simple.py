"""
Apply Page Object pattern to this tests
"""
import time

import pytest

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys

from pytest.selenium_page_object.Pages.add_books import AddBook

from pytest.selenium_page_object.tests.test_case import TestCase

from pytest.selenium_page_object.Pages.login import LoginPage

from pytest.selenium_page_object.Pages.remove_book import RemoveBook

USER = {
    'login': 'test12345678qweR',
    'password': '12345678qweR!'
}
BOOK_NAME_1 = 'Programming JavaScript Applications'
BOOK_NAME_2 = 'Learning JavaScript Design Patterns'


def find_element_by_text(driver, text, tag_name='span'):
    return driver.find_element_by_xpath(f'//{tag_name}[contains(., "{text}")]')


# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
class TestFlow(TestCase):

    def test_add_book_to_profile_flow(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.login_as_registered_user(USER)

        add_book = AddBook(self.driver)
        add_book.add_book_to_profile(BOOK_NAME_1)

        valid_and_rm_book = RemoveBook(self.driver)
        valid_and_rm_book.open_profile_page()
        valid_and_rm_book.validate_and_remove(BOOK_NAME_1)

    def test_two_add_book_to_profile_flow(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.login_as_registered_user(USER)

        add_book = AddBook(self.driver)
        add_book.add_book_to_profile(BOOK_NAME_1)
        add_book.add_book_to_profile(BOOK_NAME_2)

        valid_and_rm_book = RemoveBook(self.driver)
        valid_and_rm_book.open_profile_page()
        valid_and_rm_book.validate_and_remove(BOOK_NAME_1)
        valid_and_rm_book.validate_and_remove(BOOK_NAME_2)

