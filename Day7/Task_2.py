"""Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”"""

name = str(input('Введите имя - '))

print((lambda x: "Hello "+x)(name))