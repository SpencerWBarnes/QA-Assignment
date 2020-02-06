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

- [ ] Enter 1 : run BMI function
- [ ] Enter 2 : run Retirement Estimator function
- [ ] Enter 0 : exit
- [ ] Enter 1.1 : error message
- [ ] Enter A : error message
- [ ] Enter 3 : error message

</details>

#### BMI Functionality

<details>
<summary>runBMI</summary>

- [ ] _ : output is formatted correctly

</details>

<details>
<summary>getHeight</summary>

`foot`:
- [ ] Enter 1 : accept input
- [ ] Enter 8 : accept input
- [ ] Enter 5 : accept input
- [ ] Enter 0 : error message - too low
- [ ] Enter 9 : error message - too high
- [ ] Enter 1.1 : error message - not a whole number
- [ ] Enter A : error message - not a whole number


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

- [ ] Enter 0 : accept input
- [ ] Enter 100 : accept input
- [ ] Enter 1.1 : accept input
- [ ] Enter -0.1 : error message - too low
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

- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(10) : Met 11
- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(890) : Met 99
- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(400) : Met 50
- [ ] Enter Age(10) Salary(10) %Saved(74.0741) Goal(900) : Not met - too old

</details>