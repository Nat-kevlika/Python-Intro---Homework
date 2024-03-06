import random

n = int(input('ჩაწერეთ მთელი დადებითი რიცხვი ( 0 < n < 30): '))

random_numbers = []

for i in range(n):
    random_number = random.randint(0, 1000)
    random_numbers.append(random_number)

max_number = max(random_numbers)

#print("შემთხვევითი (random) რიცხვებია: ", random_numbers) #თუ გვინდა დავინახოთ ეს რიცხვები
print("მაქსიმალური რიცხვი არის: ", max_number)




