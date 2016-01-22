from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith goes to check out the webpage of a new to-do app
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # She is invited to enter an item immediately

        # She types "Buy peacock feathers"

        # When she hits enter, the page updates and lists
        # "1: Buy peacock feathers"
        # as an item

        # She enters another item
        # "Use peacock feathers to make a fly"

        # The page updates and she sees both items

        # She sees the site has made a unique URL for her

        # She visits the URL and finds her list is still there


if __name__ == '__main__':
    # still need to ignore warnings
    unittest.main(warnings='ignore')
