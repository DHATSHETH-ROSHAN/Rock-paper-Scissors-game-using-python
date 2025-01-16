# Rock Papper Scissors

import random

# getting the user name as input
name = input("Enter your name: ")
print(f'Welcome to Rock Paper Scissors Game, {name}')

user_score = 0
computer_score = 0

# to play the game untill the user wants to finish the game
while True:
    print("Enter your choice \n 1:Rock \n 2:Paper \n 3:Scissors \n")
    
    choice = int(input("Enteer your choice:"))
    while choice > 3 or choice < 1 :
        print("Enter your choice \n 1:Rock \n 2:Paper \n 3:Scissors \n")
        choice = int(input("Enter a valid option🫤"))
        
    # giving values as 
    if choice == 1:
        ch_n = 'Rock'
    elif choice == 2:
        ch_n = 'Paper'
    else:
        ch_n = 'Scissors'
    
    # display the choice that userr selected 
    print('Your choice is {0}'.format(ch_n))
    print('Now computers turn...')
    
    # making the computer choice 
    comp_ch = random.randint(1, 3)
    if comp_ch == 1:
        comp_n = 'Rock'
    elif comp_ch == 2:
        comp_n = 'Paper'
    else:
        comp_n = 'Scissors'
        
    # displaying computers option
    print("Computer choice is:", comp_n)
    print(ch_n, 'vs', comp_n)
    
    # gameplayy condition and selecting winner 
    if ch_n == comp_ch:
        res = "Draw"
    elif (choice == 1 and comp_ch == 2) or (comp_ch == 1 and choice == 2 ):
        res = "Paper"
    elif (choice == 1 and comp_ch == 3) or (comp_ch == 1 and choice == 3 ):
        res = "Rock"
    elif (choice == 2 and comp_ch == 3) or (comp_ch == 2 and choice == 3 ):
        res = "Scissors"

     # Print the result
    if res =="Draw":
        print("<== Damn it's a tie!!!")
    elif res == ch_n:
        user_score += 1
        print(f'You won buddy, {name}')
    else:
        computer_score +=1
        print("Computer won...Better luck next time dude")
    print(f"Score: {name} {user_score} - {computer_score} computer")
    
    print("Do you want to play again? (y/n)")
    ans = input().lower()
    if ans != 'y':
        break
print(f'Thanks for playing, {name} , !! \n Final Score: \n {name} {user_score} \n Computer {computer_score}" ')