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

class TestClient(unittest.TestCase):
  def test_getHeight_success(self):
    # Check type
    self.assertIsInstance( client.getHeight(5,5.5), float)
    
    # Check computation
    self.assertEqual( client.getHeight(1,0), 12)
    self.assertEqual( client.getHeight(8,11), 107)
    self.assertEqual( client.getHeight(1,0.1), 12.1)

  def test_validWeight_success(self):
    # Check types
    self.assertIsInstance( client.validWeight(10.1)[0], bool)
    self.assertIsInstance( client.validWeight(10.1)[1], float)

    # Check acceptable input
    self.assertEqual( client.validWeight(0.1), (True, 0.1))
    self.assertEqual( client.validWeight(100), (True, 100))
    self.assertEqual( client.validWeight(400), (True, 400))

  def test_validWeight_error(self):
    # Check unacceptable input
    self.assertEqual( client.validWeight(0)[0], False)
    self.assertEqual( client.validWeight(-1)[0], False)

if (__name__ == "__main__"):
  unittest.main()