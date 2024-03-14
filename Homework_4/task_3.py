import random

n = int(input('ჩაწერეთ მთელი დადებითი რიცხვი ( 0 < n < 1000): '))

gamyofebi = []

for i in range (1, n+1):
    if n % i == 0:
        gamyofebi.append(i)

print("gamyofebi", gamyofebi)

#########lis-ის გარეშე #####

n = int(input('ჩაწერეთ მთელი დადებითი რიცხვი ( 0 < n < 1000): '))

print("gamyofebi: ", end="")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

print()
