# Duncan is my dog, the train he operates runs in mph
dunk_speed = 30
dunk_speed_str = str(dunk_speed)
print(f"Duncan's speed is {dunk_speed_str}")

# time traveling - LATER this will be an input field
input_hours = 5

# travel distance in miles
dunk_travel = 0

print("Distance Traveled:")

counter = 1
while counter <= input_hours:
    dunk_distance = dunk_speed
    dunk_travel += dunk_distance
    print(f"Hour {counter}: {dunk_travel}")
    counter += 1
    
