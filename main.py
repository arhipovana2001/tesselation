''' Case study Tesselation
Developers: Arkhipova A.(%)
            Revtova L.(%)
'''
import turtle


def get_color_choice():
    COLORS = ['Красный', 'Желтый', 'Зеленый', 'Синий', 'Оранжевый', 'Розовый']
    print('''Допустимые цвета заливки:
1.Красный\n2.Желтый\n3.Зеленый\n4.Синий\n5.Оранжевый\n6.Розовый\n\nВыберите цвет:''')
    choice = input()
    while choice not in COLORS:
        print('Неверное значение. Введите снова:')
        choice = input()
    return choice


def get_num_hexagons():
    NUMBERS = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print('''Допустимое количество шестиугольников от 4 до 20.
Выберите количество шестиугольников''')
    choice = input()
    while int(choice) not in NUMBERS:
        print('Неверное значение. Введите снова:')
        choice = input()
    return int(choice)


color1 = get_color_choice()
color2 = get_color_choice()
number = get_num_hexagons()


turtle.done()