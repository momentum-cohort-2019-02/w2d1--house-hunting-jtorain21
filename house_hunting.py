total_cost = float(input("What is the total cost of your dream home?"))
annual_salary = float(input("What is your annual salary?"))
portion_saved = float(input("What portion of your salary will you be saving?"))
portion_saved_decimal = portion_saved / 100

portion_down_payment = total_cost * 0.25
monthly_saved = (annual_salary / 12) * portion_saved_decimal

current_savings = 0
annual_return = 0.04
months = 0

while current_savings < portion_down_payment:
    months += 1
    monthly_investment_return = current_savings * (annual_return / 12)
    current_savings += monthly_saved + monthly_investment_return

print("Number of months:", months)
