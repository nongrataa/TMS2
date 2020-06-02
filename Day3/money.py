# ввести сумму и вывести 3 рубля 45 копеек

#a = str(input("input a -  ")).split('.')

b = float(input("Input b - "))

dollar = int(b // 1)
cent = int(round((b-dollar)*100, 2))

r = ''
k = ''

if cent >= 11 and cent <= 19:
    k = 'копеек'  # print('копеек')
elif cent % 10 >= 5 and cent % 10 <= 9 or cent % 10 == 0:
    k = 'копеек'  # print('Копеек')
elif cent % 10 >= 2 and cent % 10 <= 4:
    k = 'копйки'  # print('Копейки')
elif cent % 10 == 1:
    k = 'копейка'  # print('Копейка')

if dollar >= 11 and dollar <= 19:
    r = 'рублей'  # print('Рблей)
elif dollar % 10 >= 5 and dollar % 10 <= 9:
    r = 'рублей'  # print('Рублей')
elif dollar % 10 >= 2 and dollar % 10 <= 4:
    r = 'рубля'  # print('Рубля')
elif dollar % 10 == 1:
    r = 'рубль'  # print('Рубль')

print(f'{dollar} {r}, {cent} {k}')
#
# if int(a[1]) >= 11 and int(a[1]) <= 19:
#     k = 'копеек'  # print('копеек')
# elif int(a[1]) % 10 >= 5 and int(a[1]) % 10 <= 9:
#     k = 'копеек'  # print('Копеек')
# elif int(a[1]) % 10 >= 2 and int(a[1]) % 10 <= 4:
#     k = 'копйки'  # print('Копейки')
# elif int(a[1]) % 10 == 1:
#     k = 'копейка'  # print('Копейка')
#
# if int(a[0]) >= 11 and int(a[0]) <= 19:
#     r = 'рублей'  # print('Рблей)
# elif int(a[0]) % 10 >= 5 and int(a[0]) % 10 <= 9:
#     r = 'рублей'  # print('Рублей')
# elif int(a[0]) % 10 >= 2 and int(a[0]) % 10 <= 4:
#     r = 'рубля'  # print('Рубля')
# elif int(a[0]) % 10 == 1:
#     r = 'рубль'  # print('Рубль')


#print(f'{a[0]} {r}, {a[1]} {k}')
