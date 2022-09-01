import random

player_score = 0
cpu_score = 0


def player():
    userInput = input(str('rock, paper or scissors: '))
    if userInput != 'rock' or 'scissors' or 'paper':
        userInput = input(str('please input a valid entry: '))
    return userInput


def game():
    player_score = 0
    cpu_score = 0
    while player_score or cpu_score <= 2:
        rps = ['rock', 'paper', 'scissors']
        a = random.choice(rps)
        b = player()
        print('cpu choice: ', a)

        if a == 'scissors' and b == 'rock':
            player_score += 1
        elif a == 'scissors' and b == 'paper':
            cpu_score += 1
        elif a == 'paper' and b == 'rock' :
            cpu_score += 1
        elif a == 'paper' and b == 'scissors':
            player_score += 1
        if a == 'rock' and b == 'scissors':
            cpu_score += 1
        elif a == 'rock' and b == 'paper':
            player_score += 1
        print(str(player_score), '-', str(cpu_score))

        if player_score == 3:
            print('congratulations you won!')
            if input(str('would you like to play again? ')) == 'no':
                return False
        if cpu_score == 3:
            print('sorry you lost')
            if input(str('would you like to play again? ')) == 'no':
                return False


while True:
    game()
