import random

random_numbers = [random.randint(1, 500) for i in range(100)]
#print(random_numbers)

even_count = 0
odd_count = 0

for num in random_numbers:
    if num % 2 ==0:
        even_count+=1
    else:
        odd_count+=1

numbers_dict = {'even': even_count, 'odd': odd_count}

print(numbers_dict)

