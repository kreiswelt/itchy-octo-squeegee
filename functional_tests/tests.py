from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Dede has heard about a cool new online to-do app. He goes
		# to check out its homepage
		# self.browser.get('http://localhost:8000')
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention to-do lists
		# assert 'To-Do' in browser.title, "Browser title was " + browser.title
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# He is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		# He types "Buy peacock feathers" into a text box (Dede's hobby
		# is tying fly-fishing lures)
		inputbox.send_keys('Buy peacock feathers')

		# When he hits enter, the page updates, and now the page lists
		# "1: Buy peacock feathers" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table -- its text was:\n%s" % (
				table.text)
		)

		# There is still a text box showing him to add another item. He
		# enters "Use peacock feathers to make a fly" (Dede is very methodical)
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		# The page updates again, and now shows both items on his list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		# Dede wonders whether the site will remember his list. Then he sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.
		self.fail('Finish the test!')

		# He visits that URL - his to-do list is still there.

		# Satisfied, he goes back to sleep



# if __name__ == '__main__':
# 	unittest.main()