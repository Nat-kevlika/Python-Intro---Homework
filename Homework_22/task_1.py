def read_data():
    with open("data.txt", "r") as file:
        return file.readlines()

def write_to_files(lines):
    small_lines = []
    high_lines = []

    for line in lines:
        user_name, product_name, amount, price = line.strip().split(",")
        amount = int(amount)
        price = float(price)
        total_price = amount * price

        if total_price < 10:
            small_lines.append(f"{user_name}, {product_name}, {amount}, {price}\n")
        else:
            high_lines.append(f"{user_name}, {product_name}, {amount}, {price}\n")

    with open("small.txt", "w") as small_file:
        small_file.writelines(small_lines)

    with open("high.txt", "w") as high_file:
        high_file.writelines(high_lines)

    print("Small.txt and high.txt have been created.")

def main():
    data_lines = read_data()
    write_to_files(data_lines)

if __name__ == "__main__":
    main()

