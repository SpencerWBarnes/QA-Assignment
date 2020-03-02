from browser import document

def setupEvents():
  document["calculateBMI"].bind("click", runBMI)
  document["calculateRetirement"].bind("click", runRetirementCalculator)
  print("Set up all buttons")

  document["feet"].bind("input", feetOnChange)
  document["inches"].bind("input", inchesOnChange)
  document["weight"].bind("input", weightOnChange)
  
  document["currentAge"].bind("input", currentAgeOnChange)
  document["salary"].bind("input", salaryOnChange)
  document["percentSaved"].bind("input", percentSavedOnChange)
  document["saveGoal"].bind("input", saveGoalOnChange)
  print("Set up all event listeners")

  feetOnChange("")
  inchesOnChange("")
  currentAgeOnChange("")
  percentSavedOnChange("")
  print("Ran slider's first feedback")

# Helpers associated with getting user's BMI
def runBMI(event):
  # Lead in with title
  print("\nCalculating BMI")
  # Expected input
  height = getHeight()
  print(" Height: " + str(height))

  # Expected input
  weight = getWeight()
  print(" Weight: " + str(weight))

  if (type(height) != float or type(weight) != float):
    document["bmiResult"].innerHTML = ""
    return

  print("\n Results:")
  calculateBMI(height, weight)

def getHeight():
  height = int(document["feet"].value) * 12
  print(" Feet: " + str(height))
  height = float(height) + float(document["inches"].value)
  return height

def getWeight():
  weight = document["weight"].value

  try:
    weight = float(weight)
    print(" Pounds: " + str(weight))
  except:
    # Non float values
    print("\tThat is not a number")
    return "That is not a number"

  # x > 0
  if (weight > 0):
    return weight
  else:
    print("\tThat is too low")
    return "That is too low"

def calculateBMI(height, weight):
  bmi = (weight * 0.45) / ((height * 0.025)**2)
  bmi = round(bmi,1)

  output = "Calculated BMI: " + str(bmi) + "<br> BMI Category: "

  if (bmi < 18.5):
    output = output + "Underweight"
  elif (bmi >= 18.5 and bmi <= 24.9):
    output = output + "Normal weight"
  elif (bmi >= 25 and bmi <= 29.9):
    output = output + "Overweight"
  else:
    output = output + "Obese"

  print(output)
  document["bmiResult"].innerHTML = output

# Helper associated with getting user's estimated retirement age
def runRetirementCalculator(event):
  # Lead in with title
  print("\nCalculating age of retirement")
  
  age = getCurrentAge()
  print(" Age: " + str(age))

  salary = getSalary()
  print(" Salary: " + str(salary))

  percentageSaved = getPercentSaved()
  print(" Percent Saved: " + str(percentageSaved))

  saveGoal = getSaveGoal()
  print(" Save goal: " + str(saveGoal))

  if (type(age) != int or type(salary) != float or type(percentageSaved) != float or type(saveGoal) != float):
    document["retirementResult"].innerHTML = ""
    return

  print("\n Results")
  calculateRetirementAge(age, salary, percentageSaved, saveGoal)

def getCurrentAge():
  return int(document["currentAge"].value)

def getSalary():
  salary = document["salary"].value

  try:
    salary = float(salary)
    print(" Salary: " + str(salary))
  except:
    # Non float values
    print("\tThat is not a number")
    return "That is not a number"

  # x > 0
  if (salary > 0):
    return salary
  else:
    print("\tThat is too low")
    return "That is too low"

def getPercentSaved():
  return float(document["percentSaved"].value)

def getSaveGoal():
  saveGoal = document["saveGoal"].value

  try:
    saveGoal = float(saveGoal)
  except:
    # Non float values
    print("\tThat is not a number")
    return "That is not a number"

  # x > 0
  if (saveGoal > 0):
    return saveGoal
  else:
    print("\tThat is too low")
    return "That is too low"

def calculateRetirementAge(age, salary, savingPercentage, saveGoal):
  years = saveGoal / (salary * (savingPercentage/100))
  ageMet = years + age
  ageMet = round(ageMet)

  print("-----")
  print("| Goal: ", end='')
  if (ageMet >= 100):
    print("Not met")
  else:
    print("Met")
    print("| Age: " + str(ageMet))

  print("-----\n")


# User input functions
def feetOnChange(event):
  value = document["feet"].value
  print("- onChange: Feet " + str(value))
  document["feetLabel"].textContent = "Feet: " + str(value);

def inchesOnChange(event):
  value = document["inches"].value
  print("- onChange: Inches " + str(value))
  document["inchesLabel"].textContent = "Inches: " + str(value);

def weightOnChange(event):
  value = document["weight"].value
  print("- onChange: Weight " + str(value))
  warning = ""

  try:
    value = float(value)
    # x > 0
    if (value <= 0):
      warning = "That is too low"

  except:
    # Non float values
    warning = "That is not a number"

  print("- \t " + str(warning))
  document["weightWarning"].textContent = warning;

def currentAgeOnChange(event):
  value = document["currentAge"].value
  print("- onChange: Current age " + str(value))
  document["currentAgeLabel"].textContent = "Current age: " + str(value);

def salaryOnChange(event):
  pass

def percentSavedOnChange(event):
  value = document["percentSaved"].value
  print("- onChange: Percent Saved " + str(value))
  document["percentSavedLabel"].textContent = "Percent Saved (%): " + str(value) + "%";

def saveGoalOnChange(event):
  pass