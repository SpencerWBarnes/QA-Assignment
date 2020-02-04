def main():
  while(True):
    print("Please make a selection:");
    print(" (1) Calculate BMI");
    print(" (2) Calculate retirement age");
    print(" (0) Exit");
    choice = input(" :");

    if (choice == '1'):
      pass
    elif (choice == '2'):
      pass
    elif (choice == '0'):
      break
    else:
      input("\nThat does not appear to be a choice\n")
      continue

# def runBMI():
#   pass

def getHeight():
  height = 0
  while(True):
    print("\tMust be a whole number, greater than 0, and less than 9")
    feet = input(" ft:")
    if (!feet.isdigit()):
      input("\tThat is not a whole number")
    elif (feet <= 0 or feet >= 9):
      input("\tThat is too high or too low")
    else:
      height = feet
      break

  while(True):
    print("\tMust be zero or greater and less than 12")
    inches = input(" in:")
    if (!isinstance(inches,(int,float))):
      input("\tThat is not a number")
    elif (inches < 0 || inches >= 12):
      input("\tThat is too high or too low")
    else:
      height += inches/12
      break
  return height

def getWeight():
  weight = 0
  while(True):
    print("\tMust be a number greater than 0")
    weight = input(" lb:")
    if (!isinstance(weight,(int,float))):
      input("\tThat is not a whole number")
    elif (weight < 0):
      input("\tThat is too low")
    else:
      return weight

def calculateBMI(height, weight):
  bmi = (weight * 0.45) / ((height * 0.025)**2)
  print("-----")
  print("| BMI: "+bmi)
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

# def runRetirementCalculator():
#   pass

# def getCurrentAge():
#   return int

# def getSalary():
#   return int

# def getPercentSaved():
#   return double

# def getSaveGoal():
#   return double

# def calculateRetirementAge(age, salary, savingPercentage, saveGoal):
#   return int

if (__name__ == "__main__"):
  main()