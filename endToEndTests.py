from seleniumbase import BaseCase

class HomePageTests(BaseCase):
  def test_page_load(self):
    self.assert_title("QA Assignment")