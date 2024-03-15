import random
number = random.randint(0, 100)
tries = 10
i = 0

while i < tries:
    guess = int(input("Guess a number between 0 and 100: "))
    i += 1

    if guess == number:
        print("You are the winner!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

else:
    print(f"Computer is the winner!")

