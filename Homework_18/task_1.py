import random

# rock - R
# paper - P
# scissor - S

def comp_choice():
    choices = ['R', 'P', 'S']
    return random.choice(choices)


def choose_win(your_choice, comp_choice):
    if your_choice == comp_choice:
        return "draw"
    elif (your_choice == 'R' and comp_choice == 'S') or \
            (your_choice == 'S' and comp_choice == 'P') or \
            (your_choice == 'P' and comp_choice == 'R'):
        return "you win"
    else:
        return "computer win"


def main():
    your_score = 0
    computer_score = 0

    while your_score < 3 and computer_score < 3:
        your_choice = input("Enter your choice: ").upper()
        computer_choice = comp_choice()

        print("Your choice : ", your_choice)
        print("Computer choice: ", computer_choice)

        result = choose_win(your_choice, computer_choice)
        print(result)

        if result == "you win":
            your_score += 1
        elif result == "computer win":
            computer_score += 1

        print("Your Score:", your_score)
        print("Computer Score:", computer_score)
        print()

    if your_score == 3:
        print("You win the game.")
    else:
        print("Computer wins the game.")


if __name__ == "__main__":
    main()
