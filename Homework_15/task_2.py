def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    all_nums = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 20, 99, 13, 21, 31, 37, 41, 51]
    for num in all_nums:
        if prime(num):
            print(f"{num} is a prime num.")
        else:
            print(f"{num} is not a prime num.")

if __name__ == '__main__':
    main()

