#
# Aaron Deaver

# This program calculates the time it takes to travel
# a certain distance going a specific speed.
#

#

# Get the number of miles.
miles = float(input("Enter how many miles: "))

# Get the speed in MPH.
speed = float(input("Enter the speed traveled in MPH: "))

# Calculate the travel time.
travel_time = miles / speed

# Display the travel time (formatted to 2 decimal places).
print(f"The distance should be completed in {travel_time: .2f} hours.")
