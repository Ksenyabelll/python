
import math

def calculation(a, oper, b = None):
    result = None
    if oper not in ('+', '-', '/', '*', '^', 'log', 'sqrt'):
        print('Введенного оператора не существует, введите один из предложенного списка:')
    if b == None:
        if oper == 'sqrt':
            result = math.sqrt(a)
        elif oper == 'log':
            result = math.log(a)
    else:
        if oper == '+':
            result = a + b
        elif oper == '-':
            result = a - b
        elif oper == '/':
            result = a/b
        elif oper == '*':
            result = a*b
        elif oper == '^':
            result = a**b
    return result

print(calculation(5, '/ghj' , -7))