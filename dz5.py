
# # Task 1
# m1 = set([1, 4, 6, 6, 7, 9, 10, 2, 5])
# m2 = set((1, 5, 7, 3, 3, 6, 8))
# m3 = set(( 1, 5, 7, 3, 7, 3, 6, 8))
# m4 = set(( 1, 2, 6, 2, 3, 7, 6, 10))
#
# m123 = (m1&m2&m3) - m4
# print(m123)

# # Task 2
# sr = 0
# stroka = ''
# t = ('name', 'asses', 'sity')
# tup = tuple((t[0]+str(i),i if i%2==0 else 3,t[2]+str(i)) for i in range(7))
#
# for i in tup:
#     sr += i[1]
#
# sr_asses = sr/len(tup)
#
# for k in tup:
#     if k[1] >= sr_asses:
#         stroka += k[0] + ', '
#     else:
#         continue
#
# print(f'Ученики {stroka[:-2]} в этом семестре хорошо учатся!')

