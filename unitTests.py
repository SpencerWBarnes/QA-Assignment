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
    self.assertIsInstance( client.getHeight(5,5.5), float)
    
    # Check computation
    self.assertEqual( client.getHeight(1,0), 12)
    self.assertEqual( client.getHeight(5,5.5), 65.5)
    self.assertEqual( client.getHeight(8,11.9), 107.9)

  def test_valid_weight(self):
    # Check types
    self.assertIsInstance( client.validWeight('10.1')[0], bool)
    self.assertIsInstance( client.validWeight('10.1')[1], float)

    # Check input
    self.assertEqual( client.validWeight('0.1'), (True, 0.1))
    self.assertEqual( client.validWeight('250'), (True, 250))
    self.assertEqual( client.validWeight('0')[0], False)
    self.assertEqual( client.validWeight('A')[0], False)

  def test_valid_bmi_values(self):
    # Check types
    self.assertIsInstance( client.validBMIValues(0.1,0.1), bool)

    # Check input
    self.assertEqual( client.validBMIValues(0.1,0.1), True)
    self.assertEqual( client.validBMIValues(0.1,'A'), False)
    self.assertEqual( client.validBMIValues(0.1,None), False)

  def test_get_bmi(self):
    # Check types
    self.assertIsInstance( client.getBMI(63,125)[0], float)
    self.assertIsInstance( client.getBMI(63,125)[1], str)

    # Check input
    self.assertEqual( client.getBMI(20,5.55), (10,'Underweight'))
    self.assertEqual( client.getBMI(20,10.221), (18.4,'Underweight'))
    self.assertEqual( client.getBMI(20,10.276), (18.5,'Normal weight'))
    self.assertEqual( client.getBMI(63,125), (22.7,'Normal weight'))
    self.assertEqual( client.getBMI(20,13.831), (24.9,'Normal weight'))
    self.assertEqual( client.getBMI(20,13.887), (25,'Overweight'))
    self.assertEqual( client.getBMI(20,15.276), (27.5,'Overweight'))
    self.assertEqual( client.getBMI(20,16.609), (29.9,'Overweight'))
    self.assertEqual( client.getBMI(20,16.665), (30,'Obese'))
    self.assertEqual( client.getBMI(20,22.222), (40,'Obese'))

class TestRetirementAge(unittest.TestCase):
  def test_valid_salary(self):
    # Check types
    self.assertIsInstance( client.validSalary('50000')[0], bool)
    self.assertIsInstance( client.validSalary('50000')[1], float)

    # Check inputs
    self.assertEqual( client.validSalary('0.1'), (True,0.1))
    self.assertEqual( client.validSalary('50000'), (True,50000))
    self.assertEqual( client.validSalary('0')[0], False)
    self.assertEqual( client.validSalary('A')[0], False)

  def test_valid_save_goal(self):
    # Check types
    self.assertIsInstance( client.validSaveGoal('250000')[0], bool)
    self.assertIsInstance( client.validSaveGoal('250000')[1], float)

    # Check inputs
    self.assertEqual( client.validSaveGoal('0.1'), (True,0.1))
    self.assertEqual( client.validSaveGoal('250000'), (True,250000))
    self.assertEqual( client.validSaveGoal('0')[0], False)
    self.assertEqual( client.validSaveGoal('A')[0], False)

  def test_valid_retirement_values(self):
    # Check types
    self.assertIsInstance( client.validRetirementValues(1,0.1,0.1,0.1), bool)

    # Check inputs
    self.assertEqual( client.validRetirementValues(1,0.1,0.1,0.1), True)
    self.assertEqual( client.validRetirementValues(1,'0.1',0.1,0.1), False)
    self.assertEqual( client.validRetirementValues(1,None,0.1,0.1), False)
    self.assertEqual( client.validRetirementValues(1,0.1,0.1,'0.1'), False)
    self.assertEqual( client.validRetirementValues(1,0.1,0.1,None), False)
    self.assertEqual( client.validRetirementValues(1,'0.1',0.1,'0.1'), False)
    self.assertEqual( client.validRetirementValues(1,None,0.1,None), False)

  def test_get_retirement_age(self):
    # Check types
    self.assertIsInstance( client.getRetirementAge(10,10,74.1,400)[0], bool)
    self.assertIsInstance( client.getRetirementAge(10,10,74.1,400)[1], int)

    # Check inputs
    self.assertEqual( client.getRetirementAge(98,10,74.1,10), (True,99))
    self.assertEqual( client.getRetirementAge(10,10,74.1,400), (True,50))
    self.assertEqual( client.getRetirementAge(10,10,74.1,900)[0], False)
    

if (__name__ == '__main__'):
  unittest.main()