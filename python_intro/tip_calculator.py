# Inputs

meal_cost = 100
tax_pct = 5
tip_pct = 2

# Calcuations

total_meal = meal_cost + (meal_cost * tax_pct / 100)
tip_amount = total_meal * tip_pct / 100
total_cost = total_meal + tip_amount

# Output
print('Cost, including tax:', total_meal)
print('Tip:', tip_amount)
print('Total', total_cost)
