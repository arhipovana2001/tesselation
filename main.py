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


color1 = get_color_choice()
color2 = get_color_choice()
number = get_num_hexagons()


turtle.done()
