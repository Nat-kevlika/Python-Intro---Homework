import random

random_numbers = []
for i in range(50):
    random_numb = random.randint(1, 30)
    random_numbers.append(random_numb)

new_random_numbers = []
for number in random_numbers:
    for i in range(number):
        new_random_numbers.append(number)

print("random_numbers:", random_numbers)
print("List of random numbers:", new_random_numbers)
print("length of random numbers:", len(new_random_numbers))

