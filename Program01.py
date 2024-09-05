# Program01.py
# Caleb Roge

# Step 1: Input Payroll Information
Employee_ID = int(input("Enter the employee's ID: "))
Hours_Worked = float(input("Enter the number of hours worked in a week: "))
Pay_Rate = float(input("Enter the hourly pay rate: "))
Federal_Tax_Withholding_Rate = float(input("Enter the federal tax withholding rate (as a percentage): "))
State_Tax_Withholding_Rate = float(input("Enter the state tax withholding rate (as a percentage): "))

# Step 2: Calculate the Payroll Information
GrossPay = Hours_Worked * Pay_Rate
FederalTaxDeductions = Federal_Tax_Withholding_Rate / 100 * GrossPay
StateTaxDeductions = (State_Tax_Withholding_Rate / 100 * GrossPay)
TotalDeductions = (Federal_Tax_Withholding_Rate / 100 * GrossPay) + (State_Tax_Withholding_Rate / 100 * GrossPay)
NetPay = GrossPay - TotalDeductions

# Step 3: Output the Gross Pay, Total Deduction, and Net Pay

print("\nSUMMARY")
print("-------")
print("Employee ID:",Employee_ID)
print("Hours Worked:",Hours_Worked)
print(f"Pay Rate: ${Pay_Rate}")
print(f"Gross Pay: ${GrossPay}")
print("Deductions:")
print(f"  Federal Withholding (20.0%): ${FederalTaxDeductions:.1f}")
print(f"  State Withholding (4.0%): ${StateTaxDeductions:.1f}")
print(f"  Total Deductions: ${TotalDeductions:.1f}")
print(f"Net Pay: ${NetPay}")
