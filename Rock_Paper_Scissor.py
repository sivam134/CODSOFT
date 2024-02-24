import random

list = ["rock", "paper", "scissor"]

while True:
    ccount = 0
    ucount = 0
    user = int(input("""Game Start....\n1-YES\n2-NO/Exit """))
    
    if user == 1:
        while True:  
            user_input = int(input('''
            1 Rock
            2 Paper
            3 Scissors
            '''))
            
            if user_input == 1:
                uchoice = "rock"
            elif user_input == 2:
                uchoice = "paper"
            elif user_input == 3:
                uchoice = "scissor"
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                continue
            
            choice = random.choice(list)

            print("Computer value:", choice)
            print("User value:", uchoice)

            if choice == uchoice:
                print("Game Draw")
            elif (uchoice == "rock" and choice == "scissor") or (uchoice == "paper" and choice == "rock") or (
                    uchoice == "scissor" and choice == "paper"):
                print("You Win")
                ucount += 1
            else:
                print("You Lose")
                ccount += 1

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break
    else:
        break