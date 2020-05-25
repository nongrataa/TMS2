data = "sasha 43, masha 23"


print(data.replace(',', '').split())


sasha_age=''

for i in data.replace(',', '').split():

    if i.isdigit():
        sasha_age+=i


print(sasha_age)
