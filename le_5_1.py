import json
import re

# st = 'Телефон, email: 8 800 888 77 55, kseniblokhina99@gmail.com'
# st1 = 'Телефон, email: +7 800 888 88 88, 8 800 888 99 99 kseniblokhina99@gmail.com'
# st2 = 'Телефон, email: 8-800-888-88-88, kseniblokhina99@gmail.com'
#
# rez = re.search(r'\s\d\s\d{3}\s\d{3}\s\d{2}\s\d{2}', st1)
# rez1 = re.fullmatch(r'\s\d\s\d{3}\s\d{3}\s\d{2}\s\d{2}', st2)
# rez3 = re.split(r'\s', st2)
# rez5 = re.findall(r'\W\d{2}', st)
# rez6 = re.finditer(r'\d{2}', st)
# rez7 = re.sub(r'\b\d{2}\b','**', st2)
#
# print(rez7)
# for i in rez6:
#     print(i[0], i.start())

# ip = '456.67.97.9'
# re1 = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ip)
# re2 = re.search(r'\d{1,3}\s\d{1,3}\s\d{1,3}\s\d{1,3}', ip)
#
# if re2 or re1:
#     if re1:
#         print(re1[0])
#     else:
#         print(re2[0])
# else:
#     print('IP not correct')


import csv
db = [[str((1+j)*(i+1)) for j in range(2)] for i in range(3)]
db = dict(db)
js = json.dumps(db, sort_keys = True, indent= 4 )
print(db, js)

# with open('test_name1.csv', 'w', newline= '') as f:
#     wri = csv.writer(f)
#     for r in db:
#         wri.writerow(r)

# JSON
with open('test_name2.csv', 'w') as f:
    json.dump(js.strip(), f)


