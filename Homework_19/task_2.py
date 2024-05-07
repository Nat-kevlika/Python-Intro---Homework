def count_char(input_string):
    if not input_string.isalpha():
        print("Input is not a string")
        return

    char_counts = {char: 0 for char in input_string}

    for char in input_string:
        char_counts[char] += 1

    for char, count in char_counts.items():
        print(f"{char} - {count}")

def main():
    user_input = input("Enter a string: ")
    count_char(user_input.lower())

if __name__ == "__main__":
    main()
