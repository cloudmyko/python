availableShapes = ['square']


name = input('name of shape: ')
asking = True

while asking:
    if name not in availableShapes:
        name = input('name of shape: ')
    else:
        break



class Shapes:

    def __init__(self, name):
        self.name = name
        self.running = 1

        while self.running == 1:
            if name == 'square':
                length = int(input('length: '))
                width = int(input('width: '))

                def square(l, w):
                    SQarea = l*w
                    return int(SQarea)

                print(square(length, width))
                self.running = 0
        
        def runAgain():
            again = input('would you like to run the program again? (y/n): ')
            if again.lower() == 'y':
                name = input('name of shape: ')
                g = Shapes(name)

            else:
                quit()


        if self.running == 0:
            runAgain()



s = Shapes(name)


            