from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys

import time

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits enter in the empty input box
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        time.sleep(2)

        # The home page refreshes, and there is an error message sayong
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk'+Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        time.sleep(2)

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filing some text in
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea'+Keys.ENTER)
        time.sleep(2)
        
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

        
