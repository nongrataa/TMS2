string = str(input("Input Email")).split('@')
try:
    if "gmail.com"==string[1]:
        print('@'.join(string))
    else:
        print("Eror")
except:
    print("string not supported")

print(string)

if 'gmail.com' in string:
    print(f"Имя почтового ящика - {string[0]} ")
else:
    print('DOMAIN NAME is not supported')