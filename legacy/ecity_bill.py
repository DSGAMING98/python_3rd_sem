print("========== ELECTRICITY BILL GENERATOR ==========")

consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

units = current_reading - previous_reading
energy_charge = units * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_charge = 100
net_bill = energy_charge + electricity_duty + fixed_charge

print("\n============== ELECTRICITY BILL ==============")
print(f"Consumer Name : {consumer_name}")
print(f"Consumer ID : {consumer_id}")
print(f"Units Consumed : {units:.2f} kWh")
print(f"Energy Charge : ₹{energy_charge:.2f}")
print(f"Electricity Duty (5%) : ₹{electricity_duty:.2f}")
print(f"Fixed Meter Charge : ₹{fixed_charge:.2f}")
print("----------------------------------------------")
print(f"Net Bill Amount : ₹{net_bill:.2f}")
print("==============================================")