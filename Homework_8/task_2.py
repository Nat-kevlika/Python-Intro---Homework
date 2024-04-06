### version_1 #########
a = input("Enter a word: ")

vowel = "aAeEiIoOuU"

for c in a:
    Consonant = True
    if c in vowel:
        Consonant = False
    if Consonant:
        print(c, end='')


# ### version- 2 #####
a = input("Enter a word: ")

vowel = "aAeEiIoOuU"

for c in a:
    if c not in vowel:
        print(c, end="")

