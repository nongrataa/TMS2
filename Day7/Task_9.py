"""Создать lambda функцию, которая принимает на вход неопределенное количество именных
аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}"""

f = lambda **kwargs: kwargs.key()*2
print(f(abc="1", abcabc="3", abcabcabc="4"))