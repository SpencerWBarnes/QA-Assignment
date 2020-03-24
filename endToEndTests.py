from seleniumbase import BaseCase


class HelloWorld(BaseCase):
  def test_hello_world(self):
    self.open("https://google.com")
    self.assert_title("Google")
    self.assert_title("Noodle")