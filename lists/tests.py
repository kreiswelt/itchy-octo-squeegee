from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		# For debug, use print(repr(response.content))
		# Result: b'<html>\r\n\t<title>To-Do lists</title>\r\n</html>'
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>To-Do lists</title>', response.content)
		#self.assertTrue(response.content.strip().endswith(b'</html>'))

		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)
