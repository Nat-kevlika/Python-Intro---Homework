while True:
    n = int(input("Enter integer number n, 100 <= n < 1000: "))
    if 100 <= n < 1000:
        break
    print("Enter correct number!")


count = 0
for i in range(1, n+1):
    if i % 13 ==0:
        print(i)
        count += 1
print("multiplies of 13 are: ", count)

