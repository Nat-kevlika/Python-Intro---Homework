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
    your_choice = input("enter your choice: ").upper()
    computer_choice = comp_choice()

    print("your choice : ", your_choice)
    print("computer_choice: ", computer_choice)

    result = choose_win(your_choice, computer_choice)
    print(result)

if __name__=="__main__":
    main()

