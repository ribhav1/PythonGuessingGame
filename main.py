import random

game_number = random.randint(1, 9)
chances = 0

while chances <= 5:
    guess = int(input('Guess a number between 1 and 9: '))
    chances += 1
    if guess < game_number:
        print('Too Low, guess another number: ')
    if guess > game_number:
        print('Too High, guess another number: ')
    if guess == game_number:
        print('You Win, you guessed the correct number: ' + str(game_number))
        break
if chances > 5:
    print('You Lose, the correct number was' + str(game_number))