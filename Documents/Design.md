# Units
This file is a description of the project's functional design. Due to the
simplicity of this assignment, this project will be primarily function 
based with minimal object orientation.

**void main()**
A looping main menu offering the user a number of choices.

---
**void runBMI()**
Execute the functions to get the information needed from the user, calculate the BMI, and output to the user.

---
**double getHeight()**
Get height in feet and inches from the user. Error handling will ensure feasible values are entered.
- Provided foot value is whole numbers and must be: 0 < x < 9
- Provided inch value may be double and must be: 0 <= x < 12

---
**double getWeight()**
Get weight in poounds from the user. Error handling will ensure feasiable values are entered.
- Provided weight value may be double and must be: x > 0

---
**double calculateBMI(double height, double weight)**
Calculate the user's BMI based on entered height in feet and weight in pounds using the equation from http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html and display the number and category
- Output categories must follow:
  - Underweight: x < 18.5
  - Normal weight: 18.5 <= x <= 24.9
  - Overweight: 25 <= x <= 29.9
  - Obese: x > 30

---
**void runRetirementCalculator()**
Execute the functions to get the information needed from the user, calculate the estimated retirment age, and output to the user.

---
**int getCurrentAge()**
Get the user's current age in years. Error handling will ensure feasible values are entered.
- Provided age must be a whole number and must be: 0 < x < 100

---
**int getSalary()**
Get the user's salary in US dollars. Error handling will ensure feasible values are entered.
- Provided salary may be double and must be: x > 0

---
**double getPercentSaved()**
Get the user's percentage of salary that they are saving. It is assumed that their employer is also supplying an additional 35% of their saved value. Error handling will ensure feasible values are entered.
- Provided percentage may be double and must be: 0 <= x <= 100

---
**double getSaveGoal()**
Get the user's desired savings goal in US dollars. Error handling will ensure feasible values are entered.
- Provided save goal may be double and must be: x > 0

---
**int calculateRetirementAge(int age, double salary, double savingPercentage, double saveGoal)**
Calculate the user's age once they meet their save goal for retirment. It is assumed that ages after 100 are considered not met.
- Output age is not met if: x >= 100


## Design

- main
  - runBMI
    - getHeight
    - getWeight
    - calculateBMI
  - runRetirementCalculator
    - getCurrentAge
    - getSalary
    - getPercentSaved
    - getSaveGoal
    - calculateRetirementAge