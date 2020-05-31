string = str(input("Введите строку: "))
new_string = ''
for i in range(len(string)):
    if i % 2 == 0:
        new_string += string[i]

print("Ваша строка - ", string)
print("Новая строка - ", new_string)