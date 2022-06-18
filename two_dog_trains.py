# I do not know why I am doing this

# distance in miles between Albuquerque, NM and Albany, NY
distance = 2063

# speed in mph - my dogs are the engineers
dunk_speed = 30
tony_speed = 42

"""
#this is legacy code from the old prototype with iteration
# time in hours
dunk_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tony_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while distance > dunk_distance + tony_distance:

else:
    print("crash!")
"""

print(f"Duncan's speed is {dunk_speed}")

# time traveling - LATER this will be an input field
input_hours = 50

# travel distance in miles
dunk_travel = 0
tony_travel = 0

print("Distance Traveled:")

counter = 1
while counter <= input_hours:
    dunk_distance = dunk_speed
    tony_distance = tony_speed
    dunk_travel += dunk_distance
    tony_travel += tony_distance
    total_distance = dunk_travel + tony_travel
    print("***")
    print(f"Hour {counter}: ")
    print(f"Duncan has traveled: {dunk_travel} mi.")
    print(f"Cheese Tony has traveled: {tony_travel} mi.")
    print("***")
    print()

    if distance > total_distance:
        counter += 1
    else:
        print("crash!")
        break
