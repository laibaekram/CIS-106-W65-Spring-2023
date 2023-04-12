def compute_miles_per_gallon(miles_travelled, gallons_used):
    miles_per_gallon = miles_travelled / gallons_used
    return miles_per_gallon

def compute_cost_of_gas(gallons_used):
    cost_of_gas = gallons_used * 2.50
    return cost_of_gas

destination_city = input("Enter destination city: ")
miles_travelled = float(input("Enter miles travelled: "))
gallons_used = float(input("Enter gallons used: "))

miles_per_gallon = compute_miles_per_gallon(miles_travelled, gallons_used)
cost_of_gas = compute_cost_of_gas(gallons_used)

print("Destination City:", destination_city)
print("Miles Per Gallon:", miles_per_gallon)
print("Cost of Gas: $", cost_of_gas)