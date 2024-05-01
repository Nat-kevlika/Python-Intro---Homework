import json
def read_data():
    with open("data.txt", "r") as file:
        return file.readlines()

def calculate_stats(lines):
    max_purch_users = []
    max_purch_amount = 0
    max_purch_customers = []
    max_purch_value = 0
    total_purch_value = 0
    total_purch_quantity = 0
    product_sales = {}

    for line in lines:
        user_name, product_name, amount, price = line.strip().split(", ")
        amount = int(amount)
        price = float(price)
        total_price = amount * price

        if amount > max_purch_amount:
            max_purch_users = [user_name]
            max_purch_amount = amount
        elif amount == max_purch_amount:
            max_purch_users.append(user_name)

        if total_price > max_purch_value:
            max_purch_customers = [user_name]
            max_purch_value = total_price
        elif total_price == max_purch_value:
            max_purch_customers.append(user_name)

        total_purch_value += total_price
        total_purch_quantity += amount

        product_sales[product_name] = product_sales.get(product_name, 0) + amount

    mean_purch_cost = total_purch_value / len(lines)
    mean_purch_quantity = total_purch_quantity / len(lines)

    max_sales_products = [k for k, v in product_sales.items() if v == max(product_sales.values())]

    return {
        "max_purch_users": max_purch_users,
        "max_purch_amount": max_purch_amount,
        "max_purch_customers": max_purch_customers,
        "max_purch_value": max_purch_value,
        "mean_purch_cost": mean_purch_cost,
        "mean_purch_quantity": mean_purch_quantity,
        "max_sales_products": max_sales_products
    }

def write_json(data):
    with open("stats.json", "w") as file:
        json.dump(data, file, indent=4)

def main():
    lines = read_data()
    stats = calculate_stats(lines)
    write_json(stats)
    print("Analysis done. Check stats.json.")

if __name__ == "__main__":
    main()
