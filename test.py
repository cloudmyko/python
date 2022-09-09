from time import sleep

time = int(input('time: '))

while time > 0:
    str_time = str(time)
    print(end=f'\r    :{str_time}')
    sleep(1)
    time -= 1
    if time < 10:
        str_time = f'{time} + ""'
        
    


