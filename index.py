from browser import document
import client

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

  if not(client.validBMIValues(height, weight)):
    document["bmiResult"].innerHTML = ""
    return

  print("\n Results:")
  calculateBMI(height, weight)

def getHeight():
  feet = int(document["feet"].value)
  inches = float(document["inches"].value)
  return client.getHeight(feet, inches)

def getWeight():
  weight = document["weight"].value

  (valid, weight) = client.validWeight(weight)
  if (valid):
    return weight
  return "Invalid weight value"

def calculateBMI(height, weight):
  (bmi, category) = client.getBMI(height, weight)
  output = "Calculated BMI: " + str(bmi) + "<br> BMI Category: " + str(category)

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

  percentSaved = getPercentSaved()
  print(" Percent Saved: " + str(percentSaved))

  saveGoal = getSaveGoal()
  print(" Save goal: " + str(saveGoal))

  if not(client.validRetirementValues(age, salary, percentSaved, saveGoal)):
    document["retirementResult"].innerHTML = ""
    return

  print("\n Results")
  calculateRetirementAge(age, salary, percentSaved, saveGoal)

def getCurrentAge():
  return int(document["currentAge"].value)

def getSalary():
  salary = document["salary"].value

  (valid, salary) = client.validSalary(salary)
  if (valid):
    return salary
  return "Invalid salary value"

def getPercentSaved():
  return float(document["percentSaved"].value)

def getSaveGoal():
  saveGoal = document["saveGoal"].value

  (valid, saveGoal) = client.validSaveGoal(saveGoal)

  if (valid):
    return saveGoal
  return "Invalid save goal value"

def calculateRetirementAge(age, salary, precentSaved, saveGoal):
  (met, ageMet) = client.getRetirementAge(age, salary, precentSaved, saveGoal)

  output = "Goal: "
  if (met):
    output = output + "Met <br> Age: " + str(ageMet)
  else:
    output = output + "Not met"

  document["retirementResult"].innerHTML = output


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
  (valid, value) = client.validWeight(value)

  if (valid):
    document["weightWarning"].textContent = ""
  else:
    document["weightWarning"].textContent = "Invalid weight value"

def currentAgeOnChange(event):
  value = document["currentAge"].value
  document["currentAgeLabel"].textContent = "Current age: " + str(value);

def salaryOnChange(event):
  value = document["salary"].value
  (valid, value) = client.validSalary(value)

  if (valid):
    document["salaryWarning"].textContent = ""
  else:
    document["salaryWarning"].textContent = "Invalid salary value"

def percentSavedOnChange(event):
  value = document["percentSaved"].value
  document["percentSavedLabel"].textContent = "Percent Saved (%): " + str(value) + "%";

def saveGoalOnChange(event):
  value = document["saveGoal"].value
  (valid, value) = client.validSaveGoal(value)

  if (valid):
    document["saveGoalWarning"].textContent = ""
  else:
    document["saveGoalWarning"].textContent = "Invalid save goal value"