# Tests

Tests are written in the format `<input> : <expected behavior> - <reason>` and will generally follow the order of 
1) Lower interior
2) Upper interior
3) Mid interior
4) Lower exterior
5) Upper exterior
6) Unaccepted types
---

## Unit tests

#### BMI Functionality

<details>
<summary>getHeight</summary>

- [ ] Enter (1,0) : 12 - minimum values
- [ ] Enter (5,5.5) : 65.5 - average values
- [ ] Enter (8,11.9) : 107.9 - maximum values

</details>

<details>
<summary>validWeight</summary>

- [ ] Enter 0.1 : (True,Float(0.1)) - minimum value
- [ ] Enter 250 : (True,Float(250)) - average value
- [ ] Enter 0 : (False,-) - too low
- [ ] Enter A : (False,-) - not a number

</details>

<details>
<summary>validBMIValues</summary>

- [ ] Enter (Float,Float) : True - expected types
- [ ] Enter (Float,String) : False - bad weight
- [ ] Enter (Float,None) : False - bad weight

</details>

<details>
<summary>getBMI</summary>

- [ ] Enter (20,5.55) : (10,Underweight)
- [ ] Enter (20,10.221) : (18.4,Underweight)
- [ ] Enter (20,10.276) : (18.5,Normal Weight)
- [ ] Enter (63,125) : (22.7,Normal Weight)
- [ ] Enter (20,13.831) : (24.9,Normal Weight)
- [ ] Enter (20,13.887) : (25.0,Overweight)
- [ ] Enter (20,15.276) : (27.5,Overweight)
- [ ] Enter (20,16.609) : (29.9,Overweight)
- [ ] Enter (20,16.665) : (30.0,Obese)
- [ ] Enter (20,22.22) : (40.0,Obese)

</details>

#### Retirment Age Calculator Functionality

<details>
<summary>validSalary</summary>

- [ ] Enter 0.1 : (True,Float(0.1)) - minimum value
- [ ] Enter 50000 : (True,Float(50000)) - average value
- [ ] Enter 0 : (False,-) - too low
- [ ] Enter A : (False,-) - not a number

</details>

<details>
<summary>validSaveGoal</summary>

- [ ] Enter 0.1 : (True,Float(0.1)) - minimum value
- [ ] Enter 250000 : (True,Float(250000)) - average value
- [ ] Enter 0 : (False,-) - too low
- [ ] Enter A : (False,-) - not a number

</details>

<details>
<summary>validRetirementValues</summary>

- [ ] Enter (Int,Float,Float,Float) : True - expected values
- [ ] Enter (Int,String,Float,Float) : False - bad salary
- [ ] Enter (Int,None,Float,Float) : False - bad salary
- [ ] Enter (Int,Float,Float,String) : False - bad save goal
- [ ] Enter (Int,Float,Float,None) : False - bad save goal
- [ ] Enter (Int,String,Float,String) : False - bad salary and save goal
- [ ] Enter (Int,None,Float,None) : False - bad salary and save goal

</details>

<details>
<summary>getRetirementAge</summary>

- [ ] Enter (98,10,74.1,10) : (True,99)
- [ ] Enter (10,10,74.1,400) : (True,50)
- [ ] Enter (10,10,74.1,900) : (False,-) - too old

</details>

---
## End to end tests

#### BMI Functionality

<details>
<summary>runBMI</summary>

- [x] _ : output is formatted correctly

</details>

<details>
<summary>getHeight</summary>

`foot`:
- [x] Enter 1 : accept input
- [x] Enter 8 : accept input
- [x] Enter 5 : accept input
- [x] ~~Enter 0 : error message - too low~~
- [x] ~~Enter 9 : error message - too high~~
- [x] ~~Enter 1.1 : error message - not a whole number~~
- [x] ~~Enter A : error message - not a whole number~~


`inch`:
- [x] Enter 0 : accept input
- [x] Enter 11.9 : accept input
- [x] Enter 6 : accept input
- [x] Enter -0.1 : error message - too low
- [x] Enter 12 : error message - too high
- [x] Enter A : error message - not a number

</details>

<details>
<summary>getWeight</summary>

- [x] Enter 0.1 : accept input
- [x] Enter 250 : accept input
- [x] Enter 0 : error message - too low
- [x] Enter A : error message - not a number

</details>

<details>
<summary>calculateBMI</summary>

- [x] Enter Height(1,8) Weight(5.55) : 10 Underweight
- [x] Enter Height(1,8) Weight(10.221) : 18.4 Underweight
- [x] Enter Height(1,8) Weight(10.276) : 18.5 Normal Weight
- [x] Enter Height(5,3) Weight(125) : 22.7 Normal Weight
- [x] Enter Height(1,8) Weight(13.831) : 24.9 Normal Weight
- [x] Enter Height(1,8) Weight(13.887) : 25.0 Overweight
- [x] Enter Height(1,8) Weight(15.276) : 27.5 Overweight
- [x] Enter Height(1,8) Weight(16.609) : 29.9 Overweight
- [x] Enter Height(1,8) Weight(16.665) : 30.0 Obese
- [x] Enter Height(1,8) Weight(22.22) : 40.0 Obese

</details>

#### Retirment Age Calculator Functionality

<details>
<summary>runRetirementCalculator</summary>

- [x] _ : output is formatted correctly

</details>
<details>
<summary>getCurrentAge</summary>

- [x] Enter 1 : accept input
- [x] Enter 99 : accept input
- [x] Enter 50 : accept input
- [x] Enter 0 : error message - too low
- [x] Enter 100 : error message - too high
- [x] Enter 1.1 : error message - not a whole number
- [x] Enter A : error message - not a whole number

</details>
<details>
<summary>getSalary</summary>

- [x] Enter 0.1 : accept input
- [x] Enter 50000 : accept input
- [x] Enter 0 : error message - too low
- [x] Enter A : error message - not a number

</details>
<details>
<summary>getPercentSaved</summary>

- [x] Enter 0.1 : accept input
- [x] Enter 100 : accept input
- [x] Enter 50 : accept input
- [x] Enter 0 : error message - too low
- [x] Enter 100.1 : error message - too high
- [x] Enter A : error message - not a number

</details>
<details>
<summary>getSaveGoal</summary>

- [x] Enter 0.1 : accept input
- [x] Enter 50000 : accept input
- [x] Enter 0 : error message - too low
- [x] Enter A : error message - not a number

</details>
<details>
<summary>calculateRetirementAge</summary>

- [x] Enter Age(98) Salary(10) %Saved(74.0741) Goal(10) : Met 99
- [x] Enter Age(10) Salary(10) %Saved(74.0741) Goal(400) : Met 50
- [x] Enter Age(10) Salary(10) %Saved(74.0741) Goal(900) : Not met - too old

</details>