#Sean Morrell - Aylesbury Grammar School

import math

entry = input("Enter the interest and repayment: ")

values = entry.split(" ")
interest = float(values[0])
repayment = float(values[1])

debt = 100.0

total = 0.0

while debt > 0:
    monthly_interest = math.ceil(debt * interest) / 100
    debt += monthly_interest
    monthly_repayment = math.ceil(debt * repayment) / 100
    if monthly_repayment < 50.0:
        monthly_repayment = 50.0

    if debt - monthly_repayment <= 0.0:
        total += debt
        debt = 0.0
    else:
        total += monthly_repayment
        debt -= monthly_repayment

print(math.ceil(total*100)/100)
