while True:
    try:
        expression = input()
        answ = eval(expression)
        print(str(expression) + ' = ' + str(answ))
    except:
        print('Error')