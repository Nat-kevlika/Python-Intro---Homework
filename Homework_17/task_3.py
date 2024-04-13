def main():
    my_list = [
        "banana",
        "dog",
        "Ana",
        "car",
        "laptop",
        "Python",
        "Nature",
        "elephant",
        "cat",
        "fish",
        "bird",
        "is",
        "it",
        "no"
    ]
    print("my_list: ", my_list)

    filtered_list = [word.upper() for word in my_list if len(word) <= 3]
    print("filterd list: ", filtered_list)

if __name__ == '__main__':
    main()

