
import os

file = open('test0_ksu.txt', 'r')
lines = file.readlines()

for i in range(9):
    try:
        # assert int(lines[i]) == 1, ('тут 1')
        if int(lines[i]) == 3:
            raise ZeroDivisionError
        else:
            print(int(lines[i].strip())) # IndexError
    except IndexError as er:
        print('Такой строки нет:', er)
    except ValueError as er:
        print('Некорректный тип данных:', er)
    except ZeroDivisionError:
        print('С 3 не работает')
    finally:
        print('qwert')
    # else:
    #     print('Ошибок нет')

file.close()