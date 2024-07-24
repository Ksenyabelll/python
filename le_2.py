
# # конкатенация (сложение строк)
# s1 = 'Hi '
# s2 = 'Ksu'
# print(s1 + s2)
# print(s1 * 5)
# # print(s1 * 5.3) # float не работает
# a = '1'
# print(id(a))
# a = int(a)
# print(id(a))

# # Поиск длины
# a = 32
# # print(len(a)) # с числом не работает
# a = str(a)
# print(len(a))

# # Оператор принадлежности
# stroka = 'hi Ksu, how are you'
# if 'Hi' in stroka:
#     print("Yes")
# else:
#     print("No")

# # Сравнение строк
# s1 = 'Hi'
# s2 = 'hi'
# print(s1 in s2)
# print(s1 > s2)
# print(s1 < s2)

# # Индексация
# a = 'qwerty'
# print(a[-2])

# # Срезы [x:y] - x выключительно, y - нет
# s = 'PythonKsu'
# print(s[:-1])
# print(s[::2])
#
# number = 123445679873921780723459082374089723490873529087
# while number:
#     last_num=number%10
#     number//=10
#     print(last_num, end=" ")

# s='ksksks'
# count=0
# for simbol in s:
#     if simbol=="k":
#         count+=1
# #print(simbol, end=" ")
# print(count)

# for i in range(4):
#     print(i, end = '*'*i)

# cnt = 0
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             cnt += 1
#             print(f'{cnt}  {h}:{m}:{s}')
#

# s1 = 3
# for i in range(1, s1 + 1):
#      for j in range(1, s1 + 1):
#          print(f'{j*i} - {i}*{j}', end='\t')
#      print()


# count = 0
# for i in range(1,20):
#     if i%3==0 or i%7==0 or i%2==0:
#         continue
#     else:
#         count += 1
#         print(i, end = ' ')
# print()
# print(count)

# # Список
# my_list = [6,7,0,67, 'qwe', True]
# print(my_list)
# print(my_list[::-1])
# # print(id(my_list))
# my_list[-1] = 3
# print(my_list)
# my_list[0:3] = [0,'wertyu']
# print(my_list)
# my_list[0:3] = 'a'
# print(my_list)
# # print(id(my_list))

# l1 = [4,5,6,7,8]
# l2 = [0,1,2,3,9,4,4,4,4]
# l1.append(567)
# print(l1)
# l1.extend(l2)
# print(l1)
# l1.insert(1,999)
# print(l1)
# del_ = l1.pop(0)
# print(l1, ' - ', del_)
# print(l1.index(4))
# print(l1.index(4, 12, 13))

# num = input('Введите числа: ').split(sep = ',')
# print(num)
# for e in num:
#     num[int(e)-1] = int(e)
# print(num)

# # Генератор списка
# n=m=4
# pr = ['pr']
# print(pr*m)
# l1 = [pr for i in range(n)] # comprehension
# print(l1)
# for j in l1:
#     print(j)


# l1 = [3*i for i in range(5)]
# print(l1)

num = 3
list1 = [i for i in range(num)]
l1 = [list1[j] for j in range(num)]
print(list1)
print(l1)