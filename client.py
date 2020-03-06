'''
float getHeight(feet, inches)

(bool, float) validWeight(weight)

bool validBMIValues(height, weight)

(float, string) getBMI(height, weight)
'''

def getHeight(feet, inches):
  return (int(feet)*12) + float(inches)

def validWeight(weight):
  valid = False;
  try:
    weight = float(weight)
    # x > 0
    if (weight > 0):
      valid = True;
  except:
    # Non float values
    pass

  return (valid, weight)

def validBMIValues(height, weight):
  return type(height) == float and type(weight) == float

def getBMI(height, weight):
  bmi = (weight * 0.45) / ((height * 0.025)**2)
  bmi = round(bmi,1)

  category = ""
  if (bmi < 18.5):
    category = "Underweight"
  elif (bmi >= 18.5 and bmi <= 24.9):
    category = "Normal weight"
  elif (bmi >= 25 and bmi <= 29.9):
    category = "Overweight"
  else:
    category = "Obese"

  return (bmi, category)

'''
(bool, float) validSalary(salary)

(bool, float) validSaveGoal(saveGoal)

bool validRetirementValues(age, salary, percentSaved, saveGoal)

(bool, int) getRetirementAge(age, salary, percentSaved, saveGoal)
'''

def validSalary(salary):
  valid = False;
  try:
    salary = float(salary)
    # x > 0
    if (salary > 0):
      valid = True;
  except:
    # Non float values
    pass

  return (valid, salary)

def validSaveGoal(saveGoal):
  valid = False;
  try:
    saveGoal = float(saveGoal)
    # x > 0
    if (saveGoal > 0):
      valid = True;
  except:
    # Non float values
    pass

  return (valid, saveGoal)

def validRetirementValues(age, salary, percentSaved, saveGoal):
  return type(age) == int and type(salary) == float and type(percentSaved) == float and type(saveGoal) == float

def getRetirementAge(age, salary, percentSaved, saveGoal):
  years = saveGoal / (salary * (percentSaved/100))
  ageMet = years + age
  ageMet = round(ageMet)

  met = ageMet < 100
  return (met, ageMet)