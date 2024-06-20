def temperature_data(temp):
    daily_data = []
    for day_temps in temp:
        avg_temp = sum(day_temps) / len(day_temps)
        max_temp = max(day_temps)
        min_temp = min(day_temps)
        daily_data.append((avg_temp, max_temp, min_temp))

    total_avg_temp = 0
    for avg_temp, _, _ in daily_data:
        total_avg_temp += avg_temp

    weekly_avg_temp = total_avg_temp / len(daily_data)

    return daily_data, weekly_avg_temp

temp = (
    (33, 34, 28),
    (24, 31, 27),
    (24, 23, 27),
    (28, 32, 34),
    (33, 21, 28),
    (20, 25, 31),
    (21, 31, 28)
)

daily_data, weekly_avg_temp = temperature_data(temp)

for day_index in range(len(daily_data)):
    day_number = day_index + 1
    avg_temp, max_temp, min_temp = daily_data[day_index]
    print(f"Day {day_number}:")
    print(f"  Average Temperature: {avg_temp:.2f}°C")
    print(f"  Maximum Temperature: {max_temp}°C")
    print(f"  Minimum Temperature: {min_temp}°C")

print(f"\nWeekly Average Temperature: {weekly_avg_temp:.2f}°C")
