n = int(input("Enter a positive integer (0 <= n < 10000): "))

if n >= 0 and n < 10000:
    reversed_number = 0
    orig_number = n
    while orig_number > 0:
        last_digit = orig_number % 10
        reversed_number = reversed_number * 10 + last_digit
        orig_number //= 10
    print("Reversed number:", reversed_number)

    sum_of_digits = 0
    orig_number = n
    while orig_number > 0:
        sum_of_digits += orig_number % 10
        orig_number //= 10
    print("Sum of digits:", sum_of_digits)

else:
    print("Enter a positive integer (0 <= n < 10000): ")





