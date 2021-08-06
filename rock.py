import random

def RockPapperScissors():
    user = input(" Lets play! 'r' for Rock, 'p' for Paper, 's' for Scissors   ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It is a tie'
    
    if is_win(user, computer):
        return 'You win!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
        (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(RockPapperScissors())