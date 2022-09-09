import keyboard

running = True

print('press spacebar to talk to siri')
print('if you type "hey siri" in the prompt she will carry out your next command.')
print('then press "n" for news, "s" for sports, "w" for weather or "x" to exit the program')

def siri(): 
    prompt = input('prompt: ')
    
    if prompt.lower() == 'heysiri':
        siriActive = True 
        print('press "n", "s", "w" or "x"')

        while siriActive:
            if keyboard.is_pressed('n'):
                newsContents = open('news.txt','r')
                news = newsContents.read()
                print(news)
                siriActive = False
            elif keyboard.is_pressed('s'): 
                sportsContents = open('sports.txt','r')
                sports = sportsContents.read()
                print(sports)
                siriActive = False
            elif keyboard.is_pressed('w'):
                weatherContents = open('weather.txt','r')
                weather = weatherContents.read()
                print(weather)
                siriActive = False
            elif keyboard.is_pressed('x'):
                running = False
                siriActive = False
                exit()
 

while running:
    if keyboard.is_pressed(' '):
            siri()
 


    
 