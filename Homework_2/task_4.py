car_speed = int(input("Enter the car's speed in km/h: "))

if car_speed < 30:
    category = "SLOW"
elif car_speed < 60:
    category = "MODERATE"
elif car_speed < 120:
    category = "FAST"
else:
    category = "VERY FAST"

# if 30 <= car_speed < 60 and 60 <= car_speed < 120:
#     category = "FAST"
# elif 120 <= car_speed:
#     category = "VERY FAST"

print("Car's speed category:", category)

