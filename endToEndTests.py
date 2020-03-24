from seleniumbase import BaseCase


class HelloWorld(BaseCase):
  def test_hello_world(self):
    self.open("http://localhost:8000")
    self.assert_title("QA-Assignment")
    self.assert_title("Noodle")