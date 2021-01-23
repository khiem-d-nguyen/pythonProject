while True:
    while True:
        try:
            one_x = input('please type value x one: ')
            one_x = int(one_x)
            break
        except:
            print('Error')
            continue
    while True:
        try:
            one_y = input('please type value y one: ')
            one_y = int(one_y)
            break
        except:
            print('Error')
            continue
    while True:
        try:
            two_x = input('please type value x two: ')
            two_x = int(two_x)
            break
        except:
            print('Error')
            continue
    while True:
        try:
            two_y = input('please type value y two: ')
            two_y = int(two_y)
            break
        except:
            print('Error')
            continue
    try:
        change_x = int(two_x) - int(one_x)
        change_y = int(two_y) - int(one_y)
        slope = int(change_y) / int(change_x)
        print(slope)
    except:
        print('Undefined')