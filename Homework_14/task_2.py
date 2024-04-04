from task_1 import gcd_iterative, gcd_recursive

def lcm(a, b):
    gcd_func = gcd_iterative  # iter.method
    # gcd_func = gcd_recursive  # rec.method

    gcd_value = gcd_func(a, b)
    return (a * b) // gcd_value

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if not (0 < a <= 10000 and 0 < b <= 10000):
        print("Enter numbers within the range 0 < a,b <= 10000.")
        return

    lcm_value = lcm(a, b)

    print(f"LCM of {a} and {b} is {lcm_value} (iterative method).")
    #print(f"LCM of {a} and {b} is {lcm_value} (recursive method).")

if __name__ == "__main__":
    main()

