#Вводим два слова меняем их местаим и добавляем в конце и в начале восклицательные знаки
#
string = str(input("Введите предложение "))
string_list=string.split(' ')
print(string_list)
string_list=string_list[::-1]
print(string_list)
new_string=' '.join(string_list)
print(f"! {new_string} !")
print()

#print(f"! {' '.join('Hello World'.split(' '))} !")