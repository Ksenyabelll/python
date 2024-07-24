#
# # Кортеж
# my_tuple = (3, 'qwe', '6rfkut', True, [1,4])
# my_list = [3, 'qwe', '6rfkut', True, [1,4]]
#
# a = '6rfkut'
# print(my_tuple.index(a)) if a in my_tuple else print(('No'))
#
# print(id(my_tuple))
# my_tuple[-1].append(10) # Списки менять можно
# print(my_tuple)
# print(id(my_tuple))
#
# # Последовательность из 1
# mt1 = (3,)
# print(type(mt1)) #  tuple
# mt = ((1,2),(3,4),(5,6))
# for i in mt:
#     print(i)

# # Словарь

# dict1 = {'name':'Ksu', 'age':24}
# print(dict1['age'])

# Создание словаря
# dict2 = dict(name = 'Ki', age = [27,28,29])
# print(dict2['age'][2])

# # Словари из списка кортежей [()] или ([])
# n = (['a', 10],) # или ('a', 10),
# n = dict(n)
# print(n)

# key = ['name', 'surname', 'age']
# values = ['Ksu', 'Bl', 24]
# for i in key:
#     print(i, ' : ', values[key.index(i)])
#
# # создание словарей zip
# d1 = dict(zip(key, values))
# print(d1)
# d2 = dict.fromkeys(['qwe', 'fgh'],'nothing')
# print(d2)
# d2['qwe'] = 3
# print(d2)

# # Пустой словарь
# d1 = {} #1
# d2 = dict() #2
# print((type(d1), type(d2)))

# # Изменение словарей
# d2 = dict.fromkeys(['qwe', 'fgh'],'nothing')
# d2['qwe'] = []
# d2['qwe'].append(1)
# d2['qwe'].append(3)
# print(d2)

# # Проверка ключей словаря
# i = 'qwe'
# if i in d2:
#     print(d2[i])
# else:
#     print('No')
#
# for i in d2:
#     print(i)
#
# print(d2.get('mnbvc')) # setdefault аналогично, но добавит ключ

# # распаковка словаря
#
# d1 = {'a': 10}
# print(d1)
# print(*d1)

# # добавление ключей
# d1 = dict(n = [], r = 7)
# print(d1)
# d1['loiyh'] = 4567
# print(d1)
# d2 = dict(t = 5, y = 89)
# d1.update(d2) # d1|=d2
# print(d1)

# # Генератор словарей
#
# d1 = {f'№{i}':i for i in range(9)}
# print(d1)

# # Генератор множеств
# s1 = {i for i in range(1,10,2)}
# s2 = set(range(1,10,2))
# print(s1, s2, sep = '\n')

# # Функции
# def summator(*args): #tuple
#     sum=0
#     print(type(args))
#     for i in args:
#         sum+=i
#     print(sum)
#
# summator()
# summator(1)
# summator(-1,30)
# summator(10,20 ,30,40,-100)

# def summator(**kwargs): #dict
#     print(type(kwargs))
#     for i in kwargs:
#         print([i], kwargs[i])
#
# summator(name="Иван", surname="Иванов", age=12 )
# summator(a1=2, a2="Иванов", a3=1.2, a4="sdfasdasdfasdf")

# def summator(a,b,*, d=1, f=10): #key-only parameters
#     print(a+b+d+f)
#
# summator(1,1)
# summator(1,2, d=20)
# summator(1,2, d=20, f=23)
# #summator(1,2,3,4)

def summator(a,b, /, d, f=10): #до / только позиционные
    print(a+b+d+f)
    return(5)

summator(1,1, d=20, f=15)
a = summator(1,1, d=20, f=15)
print(a)
# summator(1, b=20, d=11, f=3)