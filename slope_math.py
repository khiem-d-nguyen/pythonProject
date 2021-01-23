import random
while True:
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    two_x = random.randint(0, 10)
    two_y = random.randint(0, 10)
    answ_y = int(two_y) - int(y)
    answ_x = int(two_x) - int(x)
    Error = 'unidentified'
    while True:
        print('(' + str(x) + ', ' + str(y) + ')' + ' (' + str(two_x) + ', ' + str(two_y) + ')')
        m = input('m = ')
        try:
            if str(m) == str(Error):
                try:
                    answ_y/answ_x
                    print('Try Again')
                except:
                    print('Great Job')
                    break
            elif eval(m) == answ_y / answ_x:
                    print('Great Job!')
                    break
            else:
                print('Try Again')
                continue
        except:
            print('Error')
            continue