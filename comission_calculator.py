# Calculate comission to be paid to employees based on their sales
# Comission is 13% of the total $$$ sold
# Code should ask for the name of the employee and how much $$$ have they sold
# Code should output a phrase stating the employee name and how much $$$ they'll get paid

name = input("What is your name? ")
print(f"\nHello, {name}.\nMy name is Comission Calculator.\nI'll help you calculate your comission.\n")

sales = float(input("How much $$$ have you sold this month? "))
percentage = 0.13
comission = round(sales * percentage,2)

print(f"\nGreat {name}! Your comission is ${comission} dollars.")