input_date = input("Input date: ")

date_components = input_date.split("T")[0].split("-")
year = date_components[0]
month = date_components[1]
day = date_components[2]


time_components = input_date.split("T")[1].split(":")
hour = str(int(time_components[0]) % 12) if int(time_components[0]) > 12 else time_components[0]
minute = time_components[1]
second = time_components[2].split(".")[0]


timezone_sign = input_date[-6]
timezone_hours = input_date[-5:-3].lstrip("0")
timezone = f"{timezone_sign}{timezone_hours}"


output_date = f"{day}-{month}-{year} {hour}:{minute}:{second} {timezone}"
print("Changed format:", output_date)

