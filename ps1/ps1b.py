portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
monthly_salary = annual_salary/12
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

num_months = 1

while total_cost*portion_down_payment >= current_savings:
    if num_months % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)
    current_savings = current_savings + portion_saved*monthly_salary
    current_savings = current_savings + current_savings*r/12
    num_months = num_months + 1
    print(current_savings)
    
print("Number of months:", num_months)