import math
import random

n = int(input("Enter n (n > 1): "))

if n > 1:
    counter = 0
    for i in range(n):
        a = random.random()
        b = random.random()
        if math.sqrt(a ** 2 + b ** 2) <=1:
            counter = counter + 1
    print(f"For n = {n}, x = {4 * counter / n}")
else:
    print("Entre n, greater than 1.")

#წინა ამოცანის მსგავსად აქაც n-ის მნიშვნელობის გაზრდით x - ის მნიშვნელობა უახლოვდება pi-s მნიშვნელობას.