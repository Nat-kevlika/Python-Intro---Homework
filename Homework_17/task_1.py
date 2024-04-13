import random
def length_of_number(num):
    return len(str(num))

def main():
    random_numb = [random.randint(10, 1000000000) for i in range(100)]
    print("Random numbers:", random_numb)

    shortest_numb = min(random_numb, key=length_of_number)
    longest_numb = max(random_numb, key=length_of_number)
    asc_numbers = sorted(random_numb, key=length_of_number)
    desc_numbers = sorted(random_numb, key=length_of_number, reverse=True)


    print("Shortest number:", shortest_numb)
    print("Longest number:", longest_numb)
    print("Numbers sorted by length (ascending):", asc_numbers)
    print("Numbers sorted by length (descending):", desc_numbers)

if __name__ == '__main__':
    main()

