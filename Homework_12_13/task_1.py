def shifted_strings(input_str):
    shifted_str = []
    for c in range(len(input_str)):
        input_str = input_str[-1] + input_str[:-1]
        shifted_str.append(input_str)
    return shifted_str

def main():
    input_str = input("Enter string: ")
    for shifted_str in shifted_strings(input_str):
        print(shifted_str)

if __name__ == "__main__":
    main()
