# import le_4
# tst = lambda : le_4.age
# print(tst())
#
# def qwe(a:int) -> int:
#     return(a*2)
# print(qwe('fgh'))

# import sys
#
# def func_args(arg_cmd):
#     if len(arg_cmd) == 0:
#         return f'Список аргументов пуст'
#     else:
#         for i in range(len(arg_cmd)):
#             arg_cmd[i] = int(arg_cmd[i])
#         return f'Max - {max(arg_cmd)}, Min - {min(arg_cmd)}'
#
# if len(sys.argv) > 1:
#     arg_cmd = (sys.argv[1:])
#     print(func_args(arg_cmd))
# else:
#     print('No')


import sys

def func_args(arg_cmd):
    a = 0
    for i in range(len(arg_cmd)):
        if len(arg_cmd[i]) > a:
            a = len(arg_cmd[i])
            name = arg_cmd[i]
    return name

if len(sys.argv) > 1:
    arg_cmd = (sys.argv[1:])
    print(func_args(arg_cmd))
else:
    print('No')