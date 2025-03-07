from typing import NamedTuple

# Clearer function, better data structure
# Used NamedTuple for better readability
class SalaryDetails(NamedTuple):
    gross: float
    sss: float
    philhealth: float
    pagibig: float
    tax: float
    total_deductions: float
    net: float

def calculate_deductions(gross: float, sss: float, pagibig: float) -> SalaryDetails:
    TAX = 1875  
    philhealth = (gross * 0.05) / 2
    total_deductions = sss + philhealth + pagibig + TAX
    return SalaryDetails(gross, sss, philhealth, pagibig, TAX, total_deductions, gross - total_deductions)

def display_breakdown(details: SalaryDetails) -> None:
    # Formatted labels and currency
    print("\nSalary Breakdown\n" + "-" * 30)
    # Used _asdict to avoid repetition
    for label, value in details._asdict().items():
        print(f"{label.replace('_', ' ').title():<22} ₱{value:,.2f}")
    print("-" * 30)

def get_valid_input(prompt: str) -> float:
    """ Ensures input is a valid positive number. """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Invalid input! Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

# Get user input with validation
salary = get_valid_input("Enter your monthly salary: ")
sss = get_valid_input("Enter SSS Deduction: ")
pagibig = get_valid_input("Enter Pag-IBIG Deduction: ")

# Compute and display results, direct function call
display_breakdown(calculate_deductions(salary, sss, pagibig))