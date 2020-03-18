import unittest

import client

# mockInputValues = []
# mockInputPrompts = []
# mockOutputResults = []

# def setUpIO(inputValues):
#   global mockInputValues = inputValues
#   global mockInputPrompts = []
#   global mockOutputResults = []

#   # These are specific to the tested module
#   main.input = mockInput
#   main.print = mockOutput

# def mockInput(prompt):
#   inputResponse = str(global mockInputValues.pop(0))
#   global mockInputPrompts.append(prompt + inputResponse)
#   return inputResponse

# def mockOutput(outputResult):
#   global mockOutputResults.append(outputResult)

class TestBmi(unittest.TestCase):
  def test_get_height(self):
    # Check type
    self.assertIsInstance( client.get_height(5,5.5), float)
    
    # Check computation
    self.assertEqual( client.get_height(1,0), 12)
    self.assertEqual( client.get_height(5,5.5), 65.5)
    self.assertEqual( client.get_height(8,11.9), 107.9)

  def test_valid_weight(self):
    # Check types
    self.assertIsInstance( client.valid_weight('10.1')[0], bool)
    self.assertIsInstance( client.valid_weight('10.1')[1], float)

    # Check input
    self.assertEqual( client.valid_weight('0.1'), (True, 0.1))
    self.assertEqual( client.valid_weight('250'), (True, 250))
    self.assertEqual( client.valid_weight('0')[0], False)
    self.assertEqual( client.valid_weight('A')[0], False)

  def test_valid_bmi_values(self):
    # Check types
    self.assertIsInstance( client.valid_bmi_values(0.1,0.1), bool)

    # Check input
    self.assertEqual( client.valid_bmi_values(0.1,0.1), True)
    self.assertEqual( client.valid_bmi_values(0.1,'A'), False)
    self.assertEqual( client.valid_bmi_values(0.1,None), False)

  def test_get_bmi(self):
    # Check types
    self.assertIsInstance( client.get_bmi(63,125)[0], float)
    self.assertIsInstance( client.get_bmi(63,125)[1], str)

    # Check input
    self.assertEqual( client.get_bmi(20,5.55), (10,'Underweight'))
    self.assertEqual( client.get_bmi(20,10.221), (18.4,'Underweight'))
    self.assertEqual( client.get_bmi(20,10.276), (18.5,'Normal weight'))
    self.assertEqual( client.get_bmi(63,125), (22.7,'Normal weight'))
    self.assertEqual( client.get_bmi(20,13.831), (24.9,'Normal weight'))
    self.assertEqual( client.get_bmi(20,13.887), (25,'Overweight'))
    self.assertEqual( client.get_bmi(20,15.276), (27.5,'Overweight'))
    self.assertEqual( client.get_bmi(20,16.609), (29.9,'Overweight'))
    self.assertEqual( client.get_bmi(20,16.665), (30,'Obese'))
    self.assertEqual( client.get_bmi(20,22.222), (40,'Obese'))

class TestRetirementAge(unittest.TestCase):
  def test_valid_salary(self):
    # Check types
    self.assertIsInstance( client.valid_salary('50000')[0], bool)
    self.assertIsInstance( client.valid_salary('50000')[1], float)

    # Check inputs
    self.assertEqual( client.valid_salary('0.1'), (True,0.1))
    self.assertEqual( client.valid_salary('50000'), (True,50000))
    self.assertEqual( client.valid_salary('0')[0], False)
    self.assertEqual( client.valid_salary('A')[0], False)

  def test_valid_save_goal(self):
    # Check types
    self.assertIsInstance( client.valid_save_goal('250000')[0], bool)
    self.assertIsInstance( client.valid_save_goal('250000')[1], float)

    # Check inputs
    self.assertEqual( client.valid_save_goal('0.1'), (True,0.1))
    self.assertEqual( client.valid_save_goal('250000'), (True,250000))
    self.assertEqual( client.valid_save_goal('0')[0], False)
    self.assertEqual( client.valid_save_goal('A')[0], False)

  def test_valid_retirement_values(self):
    # Check types
    self.assertIsInstance( client.valid_retirement_values(1,0.1,0.1,0.1), bool)

    # Check inputs
    self.assertEqual( client.valid_retirement_values(1,0.1,0.1,0.1), True)
    self.assertEqual( client.valid_retirement_values(1,'0.1',0.1,0.1), False)
    self.assertEqual( client.valid_retirement_values(1,None,0.1,0.1), False)
    self.assertEqual( client.valid_retirement_values(1,0.1,0.1,'0.1'), False)
    self.assertEqual( client.valid_retirement_values(1,0.1,0.1,None), False)
    self.assertEqual( client.valid_retirement_values(1,'0.1',0.1,'0.1'), False)
    self.assertEqual( client.valid_retirement_values(1,None,0.1,None), False)

  def test_get_retirement_age(self):
    # Check types
    self.assertIsInstance( client.get_retirement_age(10,10,74.1,400)[0], bool)
    self.assertIsInstance( client.get_retirement_age(10,10,74.1,400)[1], int)

    # Check inputs
    self.assertEqual( client.get_retirement_age(98,10,74.1,10), (True,99))
    self.assertEqual( client.get_retirement_age(10,10,74.1,400), (True,50))
    self.assertEqual( client.get_retirement_age(10,10,74.1,900)[0], False)
    

if (__name__ == '__main__'):
  unittest.main()