annual_salary=float(input('Enter your annual salary:'))
portion_saved=float(input('Enter the percent of your salary to save, as a decimal:'))
total_cost=float(input('Enter the cost of your dream home:'))

portion_down_payment = 0.25
current_saving = 0
down_payment = portion_down_payment*total_cost
r=0.04
monthly_salary=annual_salary/12
k=0
portion_sav = monthly_salary*portion_saved
while True:
    k+=1
    current_saving+=current_saving*r/12
    current_saving+=monthly_salary*portion_saved
    if current_saving>=down_payment:
        break


print("Number of months:",k)