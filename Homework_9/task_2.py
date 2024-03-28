text1 = input("Enter first text: ")
text2 = input("Enter second text: ")

possible = True

if len(text1) == len(text2):
    for c in text1:
        index = text2.find(c)
        if index == -1:
            possible = False
            break
        else:
            text2 = text2[:index] + text2[index+1:]

    if len(text2) != 0:
        possible = False
else:
    possible = False

print("YES" if possible else "No")

