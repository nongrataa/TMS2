"""
Сохранить созданиый словарь в файл
Json
"""
import json

def dict_data(data, data2, data3):
    s = []
    s.extend(data)
    s.extend(data2)
    s.extend(data3)

    e = []
    e.extend(data.values())
    e.extend(data2.values())
    e.extend(data3.values())

    data4 = {}
    for i in range(0, len(s)):
        data4[s[i]] = e[i]
    return data4


data = {"name": "Sasha"}
data2 = {"Last_name": "Victorov"}
data3 = {"sur_name": "Ivanova"}

print(dict_data(data, data2, data3))
