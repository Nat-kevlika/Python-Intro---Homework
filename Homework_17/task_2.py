import random

my_list_1 = [random.randint(1, 100) for _ in range(10)]
my_list_2 = [random.randint(1, 100) for _ in range(10)]
my_list_3 = [random.randint(1, 100) for _ in range(10)]

print(my_list_1)
print(my_list_2)
print(my_list_3)

for i in range(len(my_list_1)):
    sum = my_list_1[i] + my_list_2[i]+my_list_3[i]
    print(f"Sum at indet {i}: {sum}")

