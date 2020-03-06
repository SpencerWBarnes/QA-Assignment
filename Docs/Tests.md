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

- [x] Enter (5,5.5) : Float - check type
- [x] Enter (1,0) : 12 - minimum values
- [x] Enter (5,5.5) : 65.5 - average values
- [x] Enter (8,11.9) : 107.9 - maximum values

</details>

<details>
<summary>validWeight</summary>

- [x] Enter '250' : (Bool,Float) - check types
- [x] Enter '0.1' : (True,0.1) - minimum value
- [x] Enter '250' : (True,250) - average value
- [x] Enter '0' : (False,-) - too low
- [x] Enter 'A' : (False,-) - not a number

</details>

<details>
<summary>validBMIValues</summary>

- [x] Enter (Float,Float) : bool - check type
- [x] Enter (Float,Float) : True - expected types
- [x] Enter (Float,String) : False - bad weight
- [x] Enter (Float,None) : False - bad weight

</details>

<details>
<summary>getBMI</summary>

- [x] Enter (63,125) : (Float,String) - check types
- [x] Enter (20,5.55) : (10,Underweight)
- [x] Enter (20,10.221) : (18.4,Underweight)
- [x] Enter (20,10.276) : (18.5,Normal Weight)
- [x] Enter (63,125) : (22.7,Normal Weight)
- [x] Enter (20,13.831) : (24.9,Normal Weight)
- [x] Enter (20,13.887) : (25.0,Overweight)
- [x] Enter (20,15.276) : (27.5,Overweight)
- [x] Enter (20,16.609) : (29.9,Overweight)
- [x] Enter (20,16.665) : (30.0,Obese)
- [x] Enter (20,22.22) : (40.0,Obese)

</details>

#### Retirment Age Calculator Functionality

<details>
<summary>validSalary</summary>

- [x] Enter '50000' : (Bool,Float) - check types
- [x] Enter '0.1' : (True,0.1) - minimum value
- [x] Enter '50000' : (True,50000) - average value
- [x] Enter '0' : (False,-) - too low
- [x] Enter 'A' : (False,-) - not a number

</details>

<details>
<summary>validSaveGoal</summary>

- [x] Enter '250000' : (Bool,Float) - check types
- [x] Enter '0.1' : (True,0.1) - minimum value
- [x] Enter '250000' : (True,250000) - average value
- [x] Enter '0' : (False,-) - too low
- [x] Enter 'A' : (False,-) - not a number

</details>

<details>
<summary>validRetirementValues</summary>

- [x] Enter (Int,Float,Float,Float) : Bool - check type
- [x] Enter (Int,Float,Float,Float) : True - expected values
- [x] Enter (Int,String,Float,Float) : False - bad salary
- [x] Enter (Int,None,Float,Float) : False - bad salary
- [x] Enter (Int,Float,Float,String) : False - bad save goal
- [x] Enter (Int,Float,Float,None) : False - bad save goal
- [x] Enter (Int,String,Float,String) : False - bad salary and save goal
- [x] Enter (Int,None,Float,None) : False - bad salary and save goal

</details>

<details>
<summary>getRetirementAge</summary>

- [x] Enter (10,10,74.1,400) : (Bool,Int) - check types
- [x] Enter (98,10,74.1,10) : (True,99)
- [x] Enter (10,10,74.1,400) : (True,50)
- [x] Enter (10,10,74.1,900) : (False,-) - too old

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
- [ ] Enter 1 : accept input
- [ ] Enter 8 : accept input
- [ ] Enter 5 : accept input
- [ ] ~~Enter 0 : error message - too low~~
- [ ] ~~Enter 9 : error message - too high~~
- [ ] ~~Enter 1.1 : error message - not a whole number~~
- [ ] ~~Enter A : error message - not a whole number~~


`inch`:
- [ ] Enter 0 : accept input
- [ ] Enter 11.9 : accept input
- [ ] Enter 6 : accept input
- [ ] Enter -0.1 : error message - too low
- [ ] Enter 12 : error message - too high
- [ ] Enter A : error message - not a number

</details>

<details>
<summary>getWeight</summary>

- [ ] Enter 0.1 : accept input
- [ ] Enter 250 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter A : error message - not a number

</details>

<details>
<summary>calculateBMI</summary>

- [ ] Enter Height(1,8) Weight(5.55) : 10 Underweight
- [ ] Enter Height(1,8) Weight(10.221) : 18.4 Underweight
- [ ] Enter Height(1,8) Weight(10.276) : 18.5 Normal Weight
- [ ] Enter Height(5,3) Weight(125) : 22.7 Normal Weight
- [ ] Enter Height(1,8) Weight(13.831) : 24.9 Normal Weight
- [ ] Enter Height(1,8) Weight(13.887) : 25.0 Overweight
- [ ] Enter Height(1,8) Weight(15.276) : 27.5 Overweight
- [ ] Enter Height(1,8) Weight(16.609) : 29.9 Overweight
- [ ] Enter Height(1,8) Weight(16.665) : 30.0 Obese
- [ ] Enter Height(1,8) Weight(22.22) : 40.0 Obese

</details>

#### Retirment Age Calculator Functionality

<details>
<summary>runRetirementCalculator</summary>

- [ ] _ : output is formatted correctly

</details>
<details>
<summary>getCurrentAge</summary>

- [ ] Enter 1 : accept input
- [ ] Enter 99 : accept input
- [ ] Enter 50 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter 100 : error message - too high
- [ ] Enter 1.1 : error message - not a whole number
- [ ] Enter A : error message - not a whole number

</details>
<details>
<summary>getSalary</summary>

- [ ] Enter 0.1 : accept input
- [ ] Enter 50000 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter A : error message - not a number

</details>
<details>
<summary>getPercentSaved</summary>

- [ ] Enter 0.1 : accept input
- [ ] Enter 100 : accept input
- [ ] Enter 50 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter 100.1 : error message - too high
- [ ] Enter A : error message - not a number

</details>
<details>
<summary>getSaveGoal</summary>

- [ ] Enter 0.1 : accept input
- [ ] Enter 50000 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter A : error message - not a number

</details>
<details>
<summary>calculateRetirementAge</summary>

- [ ] Enter Age(98) Salary(10) %Saved(74.0741) Goal(10) : Met 99
- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(400) : Met 50
- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(900) : Not met - too old

</details>