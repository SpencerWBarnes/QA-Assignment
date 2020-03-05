# Tests

Tests are written in the format `<input> : <expected behavior> - <reason>` and will generally follow the order of 
1) Lower interior
2) Upper interior
3) Mid interior
4) Lower exterior
5) Upper exterior
6) Unaccepted types

<details>
<summary>main</summary>

- [x] Enter 1 : run BMI function
- [x] Enter 2 : run Retirement Estimator function
- [x] Enter 0 : exit
- [x] Enter 1.1 : error message
- [x] Enter A : error message
- [x] Enter 3 : error message

</details>

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