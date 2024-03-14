import random


feri = ["clubs", "diamonds", "hearts", "spades"]
mnishvneloba = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]


random_feri = random.choice(feri)
random_mnishvneloba = random.choice(mnishvneloba)


print("Random card:", random_mnishvneloba, "of", random_feri)
