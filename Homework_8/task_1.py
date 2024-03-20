a = input("Enter a word: ")

i = 0
for c in a:
    if i % 2 ==0 and c!= "e":
        print(c, end='')

    i += 1

