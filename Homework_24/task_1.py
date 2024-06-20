import json
def get_available_dishes(recipes):
    return list(recipes.keys())

def find_stores(dish, recipes, markets):
    required_ingredients = set(recipes.get(dish, {}).get('ingredients', []))
    selected_stores = []

    while required_ingredients:
        max_unique_ingredients = set()
        max_store = None

        for store, products in markets.items():
            unique_ingredients = required_ingredients & set(products)
            if len(unique_ingredients) > len(max_unique_ingredients):
                max_unique_ingredients = unique_ingredients
                max_store = store

        if max_store is not None:
            selected_stores.append(max_store)
            required_ingredients -= max_unique_ingredients

    return selected_stores

def display_stores(stores, dish):
    if stores:
        print(f"For '{dish}', you can get all ingredients from:")
        for store in stores:
            print(f"- {store}")
    else:
        print(f"Sorry, you cannot prepare '{dish}' in this city.")

def main():
    try:
        with open('homework_1_recipes.json', 'r') as recipes_file:
            recipes = json.load(recipes_file)
    except FileNotFoundError:
        print("Error: Recipe file not found.")
        return

    try:
        with open('homework_1_markets.json', 'r') as markets_file:
            markets = json.load(markets_file)
    except FileNotFoundError:
        print("Error: Markets file not found.")
        return

    available_dishes = get_available_dishes(recipes)
    print("Available dishes:")
    for dish in available_dishes:
        print(f"- {dish}")

    dish = input("Which dish are you going to prepare? ").strip()

    selected_stores = find_stores(dish, recipes, markets)

    display_stores(selected_stores, dish)

if __name__ == "__main__":
    main()

