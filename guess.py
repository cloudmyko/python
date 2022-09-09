import random

def game():

    try:
        numRange = int(input('highest number you would like to play up to: '))
    except:
        if type(numRange) != int:
            print('please input a number!')
            numRange = int(input())
    
    if numRange > 20:
        print("let us not get ahead of ourselves\nsomething below 20\nsmh")
        numRange = int(input('20 > : '))

    number = random.randint(1,numRange)

    guesses = (numRange // 2) + 1

    guess = int(input('guess: '))
    

    while guess != number:
        guesses -= 1
        guess = int(input('guess: '))
        if guesses == 0:
            print('unfortunately, you have run out of guesses')
            break


    if guess == number or guesses == 0:
        if guess == number:
            print(f'correct! the number was {number}')
        playAgain = input('would you like to play again (y/n): ')
        if playAgain.lower() == 'y':
            game()
        else:
            exit()
        


game()

