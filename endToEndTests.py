from seleniumbase import BaseCase

class HomePageTests(BaseCase):
  def test_page_load(self):
    self.assert_title('QA Assignment')

class InputErrorTests(BaseCase):
  def test_no_errors_onload(self):
    self.assert_equal('', self.get_text('label#weightWarning'))
    self.assert_equal('', self.get_text('label#bmiResult'))
    
    self.assert_equal('', self.get_text('label#salaryWarning'))
    self.assert_equal('', self.get_text('label#saveGoalWarning'))
    self.assert_equal('', self.get_text('label#retirementResult'))