import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input('Do you want - rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('YOU WIN, the computer had ' + computer_choice)
# elif user_choice == 'paper' and computer_choice == 'rock':
    print('YOU WIN, the computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('YOU WIN, the computer had ' + computer_choice)
else:
    print('You loose :( computer wins :D')