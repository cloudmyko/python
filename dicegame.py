import random
import keyboard
import time


def game():
    rolled = False


    print('press r to roll')
    while not rolled:
        if keyboard.is_pressed('r'): # <--- receive input from the keyboard
            print('rolled')
            userRoll = random.randint(1,6)
            rolled = True
        
    cpuRoll = random.randint(1,6)
    
    time.sleep(2) # <--- delay

    print(f'you rolled : {userRoll}')
    print(f'the computer rolled {cpuRoll}')
    if userRoll > cpuRoll:
        print('you win')
    elif userRoll < cpuRoll:
        print('you lose')
    else:
        print('it is a tie!')

    print('--------------------------------------------------')

    playAgain = input('would you like to play again (y/n): ') 

    print('--------------------------------------------------')
    if playAgain.lower() == 'y':
        game()
    else:
        exit() # <--- ends the program

game()

