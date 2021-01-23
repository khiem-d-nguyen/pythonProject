import random
while True:
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    while True:
        answ = input(str(x) + ' x ' + str(y) + ' = ')
        z = x * y
        if int(answ) == z:
            print('Great Job')
            break
        else:
            print('try again')
            continue