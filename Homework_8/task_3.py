a = input("Enter a word: ")


counter = 0
while counter < 5:
    if len(a) % 2 == 0:  # If the len(a is even
        middle_left = len(a) // 2 - 1
        middle_right = len(a) // 2
        print(a[middle_left], a[middle_right])
    else:
        middle_index = len(a) // 2
        print(a[0], a[middle_index], a[-1])
    counter += 1

