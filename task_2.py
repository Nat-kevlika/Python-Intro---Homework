import datetime

year_of_birth = int(input("Enter your year of birth: "))
month_of_birth = int(input("Enter your month of birth (0-12): "))
day_of_birth = int(input("Enter your day of birth: "))

birthday = datetime.date(year_of_birth, month_of_birth, day_of_birth)

day_of_week = birthday.strftime("%A")

print("You were born on a", day_of_week + ".")

