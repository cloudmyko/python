import random

check = input('n for new user, e for existing:\n')
openfile = open('login','r+')


def captcha():
    captchaSet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    global captchaS
    captchaS = random.choices(captchaSet,k=6)
    


if check.lower() == 'n':
    username = input('choose a username:\n')
    password = input('choose a password:\n')
    passveri = input('type your password again:\n')
    if passveri == password:
        captcha()
        global captchaS
        print(captchaS)
        captchaCheck = input()
        if captchaCheck == ''.join(captchaS):
            print('thank you for creating an account.')
            openfile.write(f'{username}:{password}')
elif check.lower() == 'e':
    print('welcome!\nplease enter your username and password')
    openfile.close()
    checkUser = input()
    checkPass = input()
    if f'{checkUser}:{checkPass}' in openfile.read():
        print(f'welcome back, {checkUser}')
    else:
        checkUser = input()
        checkPass = input()
