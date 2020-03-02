from browser import document

def setupEvents():
  document["calculateBMI"].bind("click", runBMI)
  document["calculateRetirement"].bind("click", runRetirementCalculator)
  print("Set up all buttons")

  document["feet"].bind("input", feetOnChange)
  document["inches"].bind("input", inchesOnChange)
  document["weight"].bind("input", weightOnChange)
  print("Set up all event listeners")

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
    return

  print("\n Results:")
  calculateBMI(height, weight)

def getHeight():
  height = int(document["feet"].value) * 12
  print(" Feet: " + str(height))
  height = float(height) + float(document["inches"].value)
  return height

def getWeight():
  weight = 0
  
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

  print("-----")
  print("| BMI: "+ str(bmi))
  print("| Cat: ", end='')
  if (bmi < 18.5):
    print("Underweight")
  elif (bmi >= 18.5 and bmi <= 24.9):
    print("Normal weight")
  elif (bmi >= 25 and bmi <= 29.9):
    print("Overweight")
  else:
    print("Obese")

  print("-----\n")

# Helper associated with getting user's estimated retirement age
def runRetirementCalculator(event):
  # Lead in with title
  print("\nCalculating age of retirement")
  
  # Expected input
  print(" Getting current age, enter age in years")
  age = getCurrentAge()

  # Expected input
  print(" Getting annual salary, enter salary in $ per year")
  salary = getSalary()

  # Expected input
  print(" Getting percent of salary saved, enter savings as a %")
  percentageSaved = getPercentSaved()

  # Expected input
  print(" Getting save goal, enter goal in $")
  saveGoal = getSaveGoal()

  print("\n Results")
  calculateRetirementAge(age, salary, percentageSaved, saveGoal)

def getCurrentAge():
  age = 0;
  # Repeatedly ask for input until provided
  while(True):
    print("\tMust be a whole number, greater than 0, and less than 100")
    age = input("  years: ")

    try:
      age = int(age)
    except:
      # Non whole number values
      input("\tThat is not a whole number")
      continue

    # 0 < x < 100
    if (0 < age and age < 100):
      return age
    else:
      input("\tThat is too high or too low")

def getSalary():
  salary = 0;
  # Repeatedly ask for input until provided
  while(True):
    print("\tMust be a number and greater than 0")
    salary = input("  $/yr: ")

    try:
      salary = float(salary)
    except:
      # Non float values
      input("\tThat is not a number")
      continue

    # x > 0
    if (salary > 0):
      return salary
    else:
      input("\tThat is too low")

def getPercentSaved():
  percentageSaved = 0;
  # Repeatedly ask for input until provided
  while(True):
    print("\tMust be a number, 0 or greater, and 100 or less")
    percentageSaved = input("  %: ")

    try:
      percentageSaved = float(percentageSaved)
    except:
      # Non float values
      input("\tThat is not a number")
      continue

    # 0 < x <= 100
    if (0 < percentageSaved and percentageSaved <= 100):
      return percentageSaved * 1.35
    else:
      input("\tThat is too high or too low")

def getSaveGoal():
  saveGoal = 0
  # Repeatedly ask for input until provided
  while(True):
    print("\tMust be a number and greater than 0")
    saveGoal = input("  $: ")

    try:
      saveGoal = float(saveGoal)
    except:
      # Non float values
      input("\tThat is not a number")
      continue

    # x > 0
    if (saveGoal > 0):
      return saveGoal
    else:
      input("\tThat is too low")

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
    if (weight <= 0):
      warning = "That is too low"

  except:
    # Non float values
    warning = "That is not a number"

  print("-                    " + str(warning))
  document["weightWarning"].textContent = warning;