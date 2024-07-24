# name: str = 'Ksu'
# age: int = 24
#
# import numpy
#
# mx = numpy.array([[j*(i+1) for j in range(4)] for i in range(2)])
# print(mx)
# mx2 = numpy.transpose(mx)
# print(mx2)

import os

# print(os.getcwd())
# path = os.getcwd() + '\\Ksu'
#
# if not os.path.isdir('Ksu'):
#     os.mkdir('Ksu')
# else:
#     os.rmdir('Ksu')
#
# if os.path.exists('test0_ksu.txt'):
#     os.rename('test0_ksu.txt','test1_ksu.txt')
# else:
#     os.rename('test1_ksu.txt', 'test0_ksu.txt')
#
# os.remove('test0_ksu.txt')

# file = open('test0_ksu.txt',"r")
# summ = 0
# lines = file.read()
# print(type(lines))
# file.close()
#
# print(lines)

file = open('test0_ksu.txt',"r")
l = file.readline()
print(l)
while l != '':
    print(l, end = '')
    l = file.readline()

file.close()