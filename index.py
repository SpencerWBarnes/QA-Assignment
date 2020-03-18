from browser import document
import client

def setup_events():
  document['calculateBMI'].bind('click', run_bmi)
  document['calculateRetirement'].bind('click', run_retirement_calculator)
  print('Set up all buttons')

  document['feet'].bind('input', feet_on_change)
  document['inches'].bind('input', inches_on_change)
  document['weight'].bind('input', weight_on_change)
  
  document['currentAge'].bind('input', current_age_on_change)
  document['salary'].bind('input', salary_on_change)
  document['percentSaved'].bind('input', percent_saved_on_change)
  document['saveGoal'].bind('input', save_goal_on_change)
  print('Set up all event listeners')

  feet_on_change('')
  inches_on_change('')
  current_age_on_change('')
  percent_saved_on_change('')
  print("Ran slider's first feedback")

# Helpers associated with getting user's BMI
def run_bmi(event):
  # Lead in with title
  print('\nCalculating BMI')
  # Expected input
  height = get_height()
  print(' Height: ' + str(height))

  # Expected input
  weight = get_weight()
  print(' Weight: ' + str(weight))

  if not(client.validBMIValues(height, weight)):
    document['bmiResult'].innerHTML = ''
    return

  print('\n Results:')
  get_weight(height, weight)

def get_height():
  feet = int(document['feet'].value)
  inches = float(document['inches'].value)
  return client.get_height(feet, inches)

def get_weight():
  weight = document['weight'].value

  (valid, weight) = client.validWeight(weight)
  if (valid):
    return weight
  return 'Invalid weight value'

def calculate_bmi(height, weight):
  (bmi, category) = client.getBMI(height, weight)
  output = 'Calculated BMI: ' + str(bmi) + '<br> BMI Category: ' + str(category)

  print(output)
  document['bmiResult'].innerHTML = output

# Helper associated with getting user's estimated retirement age
def run_retirement_calculator(event):
  # Lead in with title
  print('\nCalculating age of retirement')
  
  age = get_current_age()
  print(' Age: ' + str(age))

  salary = get_salary()
  print(' Salary: ' + str(salary))

  percent_saved = get_percent_saved()
  print(' Percent Saved: ' + str(percent_saved))

  saveGoal = get_save_goal()
  print(' Save goal: ' + str(saveGoal))

  if not(client.validRetirementValues(age, salary, percent_saved, saveGoal)):
    document['retirementResult'].innerHTML = ''
    return

  print('\n Results')
  calculate_retirement_age(age, salary, percent_saved, saveGoal)

def get_current_age():
  return int(document['currentAge'].value)

def get_salary():
  salary = document['salary'].value

  (valid, salary) = client.validSalary(salary)
  if (valid):
    return salary
  return 'Invalid salary value'

def get_percent_saved():
  return float(document['percentSaved'].value)

def get_save_goal():
  saveGoal = document['saveGoal'].value

  (valid, saveGoal) = client.validSaveGoal(saveGoal)

  if (valid):
    return saveGoal
  return 'Invalid save goal value'

def calculate_retirement_age(age, salary, precentSaved, saveGoal):
  (met, ageMet) = client.getRetirementAge(age, salary, precentSaved, saveGoal)

  output = 'Goal: '
  if (met):
    output = output + 'Met <br> Age: ' + str(ageMet)
  else:
    output = output + 'Not met'

  document['retirementResult'].innerHTML = output


# User input functions
def feet_on_change(event):
  value = document['feet'].value
  print('- onChange: Feet ' + str(value))
  document['feetLabel'].textContent = 'Feet: ' + str(value);

def inches_on_change(event):
  value = document['inches'].value
  print('- onChange: Inches ' + str(value))
  document['inchesLabel'].textContent = 'Inches: ' + str(value);

def weight_on_change(event):
  value = document['weight'].value
  (valid, value) = client.validWeight(value)

  if (valid):
    document['weightWarning'].textContent = ''
  else:
    document['weightWarning'].textContent = 'Invalid weight value'

def current_age_on_change(event):
  value = document['currentAge'].value
  document['currentAgeLabel'].textContent = 'Current age: ' + str(value);

def salary_on_change(event):
  value = document['salary'].value
  (valid, value) = client.validSalary(value)

  if (valid):
    document['salaryWarning'].textContent = ''
  else:
    document['salaryWarning'].textContent = 'Invalid salary value'

def percent_saved_on_change(event):
  value = document['percentSaved'].value
  document['percentSavedLabel'].textContent = 'Percent Saved (%): ' + str(value) + '%';

def save_goal_on_change(event):
  value = document['saveGoal'].value
  (valid, value) = client.validSaveGoal(value)

  if (valid):
    document['saveGoalWarning'].textContent = ''
  else:
    document['saveGoalWarning'].textContent = 'Invalid save goal value'