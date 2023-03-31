portion_down_payment = 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
monthly_salary = annual_salary/12
semi_annual_raise = 0.07
portion_saved = 0.5
portion_min = 0
portion_max = 1
bisection_search = 0
max_savings = 0

#To count max savings, to see if it's possible to save in 36 months
for months in range(1,37): #starts from month 1 to month 36
    if months % 6 == 0:
        monthly_salary = monthly_salary * (1 + semi_annual_raise)
    max_savings = max_savings + monthly_salary
    max_savings = max_savings + max_savings*r/12
if max_savings < portion_down_payment*total_cost:
    print("It is not possible to pay the down payment in three years.")

while abs(current_savings - portion_down_payment*total_cost) > 100 and max_savings > portion_down_payment*total_cost:
    #Resetting these value to recount savings for 36 months again
    current_savings = 0
    monthly_salary = annual_salary/12

    #To count total savings in 36 months
    for months in range(1,37): #starts from month 1 to month 36
        if months % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
        current_savings = current_savings + portion_saved*monthly_salary
        current_savings = current_savings + current_savings*r/12

    #Bisection search, with the condition of total savings in 36 months less / more than the value.    
    if current_savings < portion_down_payment*total_cost:
        portion_min = portion_saved
    else:
        portion_max = portion_saved
    portion_saved = (portion_min + portion_max)/2
    bisection_search = bisection_search + 1

if max_savings > portion_down_payment*total_cost:
    print("Best savings rate: ", portion_saved)
    print("Steps in bisection search: ", bisection_search)