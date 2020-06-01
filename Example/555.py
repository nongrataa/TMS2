string = str(input("Input Email")).split('@')
print(string)

if 'gmail.com' in string:
    print(f"Имя почтового ящика - {string[0]} ")
else:
    print('DOMAIN NAME is not supported')