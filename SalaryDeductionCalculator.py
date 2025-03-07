def compute_deductions(salary, sss, pagibig):
    tax =  1875  #Assuming fixed value for simplicity. (gi hardcode nanako ang value since constant/fixed value nmn daw ni - eros)
    philhealth = (salary * 0.05) / 2
    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    return [salary, sss, philhealth, pagibig, tax, deductions, net_salary]


def display(results):

    print("Gross Salary:", results[0])
    print("SSS Deduction:", results[1])
    print("PhilHealth Deduction:", results[2])
    print("Pag-IBIG Deduction:", results[3])
    print("Tax Deduction:", results[4])
    print("Total Deductions:", results[5])
    print("Net Salary:", results[6])


salary = float(input("Enter your monthly salary: "))
sss =  float(input("Enter SSS Deduction: "))
pagibig =  float(input("Enter Pag-ibig Deduction: "))


results = compute_deductions(salary, sss, pagibig)

display(results)

#Akong rang gi change kay gipahimoan nakog functions ang pag display, 