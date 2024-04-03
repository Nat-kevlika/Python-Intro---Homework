def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if not (0 < a <= 10000 and 0 < b <= 10000):
        print("Enter numbers within the range 0 < a,b <= 10000.")
        return

    gcd_iter = gcd_iterative(a, b)
    gcd_rec = gcd_recursive(a, b)

    print(f"GCD of {a} and {b} is {gcd_iter} (iterative method).")
    print(f"GCD of {a} and {b} is {gcd_rec} (recursive method).")


if __name__ == "__main__":
    main()

