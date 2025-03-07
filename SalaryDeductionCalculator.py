from typing import NamedTuple

#clearer function, better data structure
#used namedtuple for better readability
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
    #added formatted labels and currency
    print("\nSalary Breakdown\n" + "-" * 30)
    #used _asdict to avoid repitition
    for label, value in details._asdict().items():
        print(f"{label.replace('_', ' ').title():<22} ₱{value:,.2f}")
    print("-" * 30)

#user input
salary = float(input("Enter your monthly salary: "))
sss = float(input("Enter SSS Deduction: "))
pagibig = float(input("Enter Pag-IBIG Deduction: "))

#compute and display results, direct function call
display_breakdown(calculate_deductions(salary, sss, pagibig))