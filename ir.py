
# 1.1

# a = (1, 1, 2, 2, 4, 7, 9, 37, 95, 18)
# b = (1, 2, 3, 4, 17, 19, 27, 5, 18)
#
# un_list = list(set(a)&set(b))
# print(un_list)

# 1.3

# n = input('Entry n: ')
# sum = 0
# for i in range(4):
#     num = (f'{n}'*(i+1))
#     sum +=int(num)
# print(sum)

# 2.1

# n = 'Test.py'
#
# try:
#     if '.' in n:
#         for i in range(len(n)):
#             if n[i] == '.':
#                 print(n[i:])
#             else:
#                 continue
#     else:
#         raise Exception
# except:
#     print('Исключение - нет типа файла')

# 2.2

# number = [1, 4, 10, 25, 30, 28, -6, -20, 0]
# num = []
# l_f = lambda n: num.append(n) if n%10 == 0 else ''
# for n in number:
#     l_f(n)
#
# print(num)

# 2.3
# l = []
# file = open('ir.txt', 'r')
# lines = file.readlines()
# for i in range(len(lines)):
#     l.append(lines[i].strip())
# file.close()
#
# print(max(l, key=len))
# print(max(l, key=l.count))


# 1.2
# itog = ''
#
# dict1 = dict({'a':1000, 'b':14, 'c':975, 'd':400,'e':15})
# s_v = sorted(dict1.values())
# print(s_v)
# sorted_dict = {}
#
# for i in s_v[::-1]:
#     for j in dict1:
#         if i == dict1[j]:
#             itog += j
#
# print(itog[:3])


