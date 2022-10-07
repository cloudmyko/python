availableShapes = ['square', 'triangle', 'circle']


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
        self.running = True

        while self.running:
            if name == 'square':
                length = int(input('length: '))
                width = int(input('width: '))

                def square(l, w):
                    SQarea = l*w
                    return int(SQarea)

                print(square(length, width))
                self.running = False

            if name == 'triangle':
                base = int(input('base of the triangle: '))
                height = int(input('height of the triangle: '))

                def triangle(b, h):
                    TRarea = b*h
                    return int(TRarea)

                print(triangle(base, height))
                self.running = False

            if name == 'circle':
                radius = int(input('radius of the circle: '))

                def circle(r):
                    pi = 3.14159265359
                    circArea = (r**2) * pi
                    return circArea

                print(circle(radius))
                self.running = False

        def runAgain():
            again = input('would you like to run the program again? (y/n): ')
            if again.lower() == 'y':
                name = input('name of shape: ')
                g = Shapes(name)

            else:
                quit()


        if self.running == True:
            runAgain()



s = Shapes(name)


            