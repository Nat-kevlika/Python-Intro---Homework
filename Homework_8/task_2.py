### version_1 #########
a = input("Enter a word: ")

xmovani = "aAeEiIoOuU"

for c in a:
    tanxmovani = True
    if c in xmovani:
        tanxmovani = False
    if tanxmovani:
        print(c, end='')


# ### version- 2 #####
a = input("Enter a word: ")

xmovani = "aAeEiIoOuU"

for c in a:
    if c not in xmovani:
        print(c, end="")
