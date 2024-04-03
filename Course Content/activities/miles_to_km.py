# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name


first_name = input("What is your name?\n")
distance_in_km = input("Distance in km:\n")
# calculation:
distance_in_m = float(distance_in_km) / 1.609

print(f"Hi, {first_name.title()}  {distance_in_km} km is equivalent to {round(distance_in_m, 1)} miles!")
