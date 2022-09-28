
def weightConvert():

    weight = int(input('weight value: '))
    metric = input('(k)g or (l)bs: ')
    poundMulti = 2.20462
    kgMulti = 0.453592

    if metric.lower() == 'k':
        print(weight * poundMulti) # <--- converts to pounds
    elif metric.lower() == 'l':
        print(weight * kgMulti) # <--- converts to kilograms
    else:
        weightConvert()

weightConvert()