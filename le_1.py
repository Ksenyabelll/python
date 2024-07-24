# # Присвоение
# a = b = 1
# print(a and b)

# # Создание переменной
# name = 'Ksenya'
# surname = 'Blokhina'
# patr = 'Olegovna'
# age = 24
# # 1test = 'qwerty'
# # if  = 10
# число = 12
# число == a # сравнение, а не присвоение
# print(число == a )
# print() # Enter
# print(a)

# # Input
# print('Entry name:')
# name = input()
# surname, age = input('Entry surname and age:'), int(input())
# print('Hi,', name, age, surname)
# age = True
# print(age)

# # Мат действия
# a = 15
# b = 7
# print(a/b)
# print(a//b) # По модулю
# print(a%b)
# print(b/a)
# print(b//a)
# print(b%a)

# # Print
# a = 1
# b = 2
# c = 3
# print(a,b,c, sep = '\n', end = '___')
# print(a,b,c, sep = '\n')

# # Форматирование
# a = 3
# b = 'qwerty'
# c = 1.2
# print('%d - целое число'%(a))
# print('%d one , %d two , %f'%(a,c,c))
# print('{1} one , {0} two , {2} three, {age}'.format(a,c, 500, b, age = 24))
# print('{1} one , {0} two , {2} three, {age:f}'.format(a,c, 500, b, age = 24))
# print('{0:10.3f}, {0:10d}'.format((1)))
# print('{0:010.3f}, {0:010d}'.format((1)))
# print('{0:>010.3f}, {0:<010d}'.format((1)))
# print('{0:^10.3f}, {0:^010d}'.format((1)))
# print('{0:^10.3f}, {0:=^010d}'.format((-1)))
# print(f'{123} ttttttt {a*c}')

# # Import
# # 2 - способ импортирвоания
# from math import pi, e
# print(pi, e)
#
# # # 3 - способ импортирвоания
# from math import pi as p
# pi= "Пифагор"
# print(pi,p)
#
# # 4 - способ импортирвоания
# import math
# print(pi, e)

# Циклы
n = int(input('Число: '))
if n != 0:
    if n>0:
        print('Положительное')
    else:
        print('Отрицательное')
else:
    print('Error')