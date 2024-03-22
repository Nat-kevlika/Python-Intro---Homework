n = int(input("Enter a positive integer n , 0 < n <= 1000:  "))

if n > 0 and n <= 1000:
    print(n, end=" ")

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        print("->", n, end=" ")
else:
    print("Enter a positive integer n, 0 < n <= 1000: ")

