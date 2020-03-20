''' Case study Tesselation
Developers: Arkhipova A.(%)
            Revtova L.(%)
'''
import turtle
from math import cos, pi, sin


def get_color_choice():
    COLORS = ['red', 'yellow', 'green', 'blue', 'orange', 'pink']
    print('''Acceptable fill colors:
1.red\n2.yellow\n3.green\n4.blue\n5.orange\n6.pink\n\nВыберите цвет:''')
    choice = input()
    while choice not in COLORS:
        print('Incorrect value. Enter again:')
        choice = input()
    return choice


def get_num_hexagons():
    NUMBERS = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print('''The allowed number of hexagons is from 4 to 20.
Select the number of hexagons:''')
    choice = input()
    while int(choice) not in NUMBERS:
        print('Incorrect value. Enter again:')
        choice = input()
    return int(choice)


def draw_hexagons(start_x, start_y, number, color1, color2):
    screen = t.Screen()
    screen.setup(600, 600)
    hexagon1 = int(number / 2)
    hexagon2 = number - hexagon1
    PIX = 500
    d = PIX / number
    y = ((d / 2) / (cos(pi / 6)))
    x = (sin(pi / 6) * y)
    mn1 = {0, 1, 4, 5, 8, 9, 12, 13, 16, 17}
    t.speed(0)
    t.up()

    def one_line(color1, color2):
        for _ in range(hexagon2):
            t.right(30)
            t.down()
            t.begin_fill()
            t.color(color1)
            for _ in range(6):
                t.fd(y)
                t.right(60)
            t.end_fill()
            t.up()
            t.left(30)
            t.fd(d + d)
        if number % 2 == 0:
            t.bk((number - 1) * d)
        elif number % 2 != 0:
            t.bk(number * d)

        for _ in range(hexagon1):
            t.right(30)
            t.down()
            t.begin_fill()
            t.color(color2)
            for _ in range(6):
                t.fd(y)
                t.right(60)
            t.end_fill()
            t.up()
            t.left(30)
            t.fd(d + d)
            
    for i in range(number):
        if i % 2 == 0:
            t.goto(start_x, start_y - (y + x) * i)
            if i in mn1:
                one_line(color1, color2)
            else:
                one_line(color2, color1)
        elif i % 2 != 0:
            t.goto(start_x - d / 2, start_y - (y + x) * i)
            if i in mn1:
                one_line(color1, color2)
            else:
                one_line(color2, color1)


draw_hexagons(-190, 245, get_num_hexagons(), get_color_choice(), get_color_choice())
turtle.done()
