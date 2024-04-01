n = int(input("Enter n (n > 1): "))

if n > 1:
    x = 0
    for i in range(1, n + 1):
        x += (-1) ** (i + 1) * (1 / (2 * i - 1))
    x *= 4
    print(f"For n = {n}, x = {x}")
else:
    print("Entre n, greater than 1.")

# n-ის ზრდასთან ერთად x-ის მნიშვნელობა უახლოვდება pi-ს მნიშვნელობას. ლაიბნიცის ფორმულა pi-სთვის.

# numbers = [10, 100, 10000, 100000]
#
# for n in numbers:
#     x = 0
#     for i in range(1, n + 1):
#         x += (-1) ** (i + 1) * (1 / (2 * i - 1))
#     x *= 4
#     print(f"For n = {n}, x = {x}")

