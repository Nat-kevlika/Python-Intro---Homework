n = int(input("Enter a number n, 0 < n < 10: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

i = n - 1
while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i -= 1

