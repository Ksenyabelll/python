
import os

def fu_os(ar):
    flag = True
    for i in range(2,ar):
        if ar%i == 0:
            flag = False
            return str(flag)
    return str(flag)

file = open('test0_ksu.txt','r')
file2 = open('test1_ksu.txt', 'w')
lines = file.readlines()
for l in lines:
    file2.write(l.strip() + fu_os(int(l)) + '\n')

file.close()
file2.close()




