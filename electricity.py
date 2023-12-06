unit_charges = float(input("Enter the electricity unit charges: "))

if unit_charges <= 50:
    total_bill = unit_charges * 0.50
elif unit_charges <= 150:
    total_bill = (50 * 0.50) + ((unit_charges - 50) * 0.75)
elif unit_charges <= 250:
    total_bill = (50 * 0.50) + (100 * 0.75) + ((unit_charges - 150) * 1.20)
else:
    total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((unit_charges - 250) * 1.50)

total_bill_with_surcharge = total_bill + (total_bill * 0.20)
print("Total Electricity Bill:", total_bill_with_surcharge)
