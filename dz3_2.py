
num = input('Введите числа: ').split(sep = ' ')
# print(num)
new_num = []

for i in range(len(num)):
    a = 'X'*(int(num[i])//10)
    if int(num[i])%10 == 9:
        a+= 'IX'
    elif int(num[i])%5 == 4:
        a+= 'IV'
    else:
        a+= 'V'*((int(num[i])%10)//5)
        a+= 'I'*((int(num[i])%10)%5)
    new_num.append(a)

print(new_num)


