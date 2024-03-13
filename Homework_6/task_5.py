n = int(input("Enter a number n, 0 < n < 10: "))

j = 0
while j < n:

    space = n - j - 1
    while space > 0:
        print(" ", end="")
        space -= 1

    i = j
    while i >= 0:
        print(i, end="")
        i -= 1

    i = 1
    while i <= j:
        print(i, end="")
        i += 1

    print()
    j += 1

