## I.	Technical debt identified
* **Hardcoded Tax Value:** The tax deduction is a fixed value (tax = 1875), which lacks flexibility if tax rates change or vary based on salary.
* **Lack of Modularity:** The program directly interacts with the user (input() calls inside get_valid_input()) instead of separating input handling from computation. This makes it harder to test.
* **Limited Error Handling:** The get_valid_input() function only checks for negative values but does not handle other edge cases like extremely high values.
* **Magic Numbers:** The PhilHealth computation uses 0.05 / 2, which should be replaced with a named constant for clarity.
* **List-Based Return Structure:** The compute_deductions() function returns a list, making it less readable and maintainable when accessing values. A dictionary or a named tuple would be clearer.

## II.	Refactoring improvements made
* **Used Constants:** Defined tax and PhilHealth rate constants for better maintainability.
* **Improved Data Structure:** Changed the return type of compute_deductions() to a dictionary for better readability.
* **Separated Concerns:** Removed direct input() calls from computation functions, allowing better unit testing.
* **Enhanced Error Handling:** Implemented checks for unrealistic values (e.g., salary too low to cover deductions).
* **Code Readability Improvements:** Used f-strings and clear variable names.

## III.	Challenges faced & solutions
* **Challenge:** The function originally returned a list, making it difficult to access specific values.
  - Solution: A dictionary stores results with meaningful keys for easier access.
* **Challenge:** The hardcoded tax value limits flexibility.
  - Solution: Introduced a tax_rate parameter, making it configurable.
* **Challenge:** The PhilHealth calculation used an unclear magic number.
  - Solution: Introduced a named constant (philhealth_rate=0.05).
* **Challenge:** The original code tightly coupled user input with computation, making testing difficult.
  - Solution: Refactored input handling to be separate from the computation, allowing unit tests to call compute_deductions() directly.
