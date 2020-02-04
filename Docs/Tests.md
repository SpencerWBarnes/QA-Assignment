# Tests

<details>
<summary>main</summary>

``` diff
- Execute BMI function
- Execute Retirement Estimator function
- Exit
- Enter non-available choice
```
</details>

#### BMI Functionality

<details>
<summary>runBMI</summary>

```diff
- Ensure output is formatted correctly
```
</details>

<details>
<summary>getHeight</summary>

```diff
- Enter negative value for `foot` and `inch`
- Enter 0 for `foot`
- Enter 0 for `inch`
- Enter double for `foot`
- Enter double for `inch`
- Enter value > 12 for `inch`
- Enter value > 9 for `foot`
- Enter alphabetic characters
```
</details>

<details>
<summary>getWeight</summary>

```diff
- Enter negative value
- Enter 0
- Enter positive value
- Enter double value
- Enter alphabetic characters
```
</details>

<details>
<summary>calculateBMI</summary>

```diff
- Ensure value is calculated correctly
- Achieve BMI 18.4
- Achieve BMI 18.5
- Achieve BMI 24.9
- Achieve BMI 25
- Achieve BMI 29.9
- Achieve BMI 30
```
</details>

#### Retirment Age Calculator Functionality

<details>
<summary>runRetirementCalculator</summary>

```diff
- Ensure output is formatted correctly
```
</details>
<details>
<summary>getCurrentAge</summary>

```diff
- Enter negative value
- Enter 0
- Enter 1
- Enter 99
- Enter 100
- Enter double value
- Enter alphabetic characters
```
</details>
<details>
<summary>getSalary</summary>

```diff
- Enter negative value
- Enter 0
- Enter double value
- Enter alphabetic characters
```
</details>
<details>
<summary>getPercentSaved</summary>

```diff
- Enter negative value
- Enter 0
- Enter 100
- Enter 101
- Enter double value
- Enter alphabetic characters
```
</details>
<details>
<summary>getSaveGoal</summary>

```diff
- Enter negative value
- Enter 0
- Enter double value
- Enter alphabetic characters
```
</details>
<details>
<summary>calculateRetirementAge</summary>

```diff
- Ensure value is calculated correctly
- Achieve value less than 100
- Achieve value equal to 100
- Achieve value greater than 100
- Achieve value less than current age
```
</details>