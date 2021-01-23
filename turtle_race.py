import turtle
turtle.color('black', 'blue')
turtle_2 = turtle.clone()
turtle.speed(0)
turtle_2.speed(0)
turtle_2.color('black', 'red')
turtle.penup()
turtle_2.penup()
turtle.goto(-250, 50)
turtle_2.goto(-250, -50)
turtle.shape('turtle')
turtle_2.shape('turtle')
base_draw = turtle.clone()
base_draw.hideturtle()
base_draw.penup()
base_draw.goto(250, 25)
base_draw.pendown()
base_draw.begin_fill()
base_draw.color('black', 'light blue')
base_draw.circle(25)
base_draw.penup()
base_draw.end_fill()
base_draw.begin_fill()
base_draw.goto(250, -25)
base_draw.pendown()
base_draw.color('black', 'pink')
base_draw.circle(-25)
base_draw.end_fill()
turtle.pendown()
turtle_2.pendown()
xcor_turtle = -250
xcor_turtle_2 = -250
turtle.speed(5)
turtle_2.speed(5)
import random
while xcor_turtle != 250 and xcor_turtle_2 != 250:
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    answ = input(str(x) + ' x ' + str(y) + ' = ')
    z = x * y
    if int(answ) == z:
        turtle.forward(50)
        xcor_turtle = xcor_turtle + 50
        print('Great Job')
    else:
        print('Maybe Next Time')
    x = random.randint(1, 12)
    y = random.randint(1, 12)
    answ = input(str(x) + ' x ' + str(y) + ' = ')
    z = x * y
    if int(answ) == z:
        turtle_2.forward(50)
        xcor_turtle_2 = xcor_turtle_2 + 50
        print('Great Job')
    else:
        print('Maybe Next Time')
if xcor_turtle == 250 and xcor_turtle_2 == 250:
    print('Draw!')
elif xcor_turtle == 250:
    print('Blue Wins!')
elif xcor_turtle_2 == 250:
    print('Red Wins!')
turtle.done()