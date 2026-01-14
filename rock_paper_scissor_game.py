import random

emojis = {'r':'🪨','p':'📃','s':'✂️'}
choices = ('r','p','s')
while True:

    user_choice = input('Rock,Paper,Scissors? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue

    computer_choices = random.choice(choices)

    print(f'You Choose {emojis[user_choice]}')
    print(f'Computer Choose {emojis[computer_choices]}')

    if user_choice == computer_choices:
        print('Tie!')

    elif (
    (user_choice == 'r' and computer_choices == 's') or
    (user_choice == 's' and computer_choices == 'p') or
    (user_choice == 'p' and computer_choices == 'r')):
        print('you Win')

    else:
        print('You Lose')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break