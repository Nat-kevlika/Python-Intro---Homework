from task_1 import shifted_strings

def check_shifted(a, b):
    shifted_strings_a = shifted_strings(a)
    return b in shifted_strings_a

def main():
    a = input("Input a: ")
    b = input("Input b: ")

    shifted = check_shifted(a, b)
    if shifted:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
