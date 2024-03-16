n = int(input("Enter a positive number n , 0 <= n < 20:  "))

if n >= 0 and n < 20:
    if n == 0:
        print("0")
    elif n == 1:
        print(" 0 1")
    else:
        a, b = 0, 1
        print(0, 1, end=" ")
        counter = 2
        while counter < n:
            sum = a + b
            print(sum, end=" ")
            a, b = b, sum
            counter += 1

else:
    print("Enter correct number: ")

