data = "sasha 43, masha 23"
change_person = False
counter = 0

print(data.replace(',', '').split())

sasha_age = ''
masha_age = ''

for i in data.replace(',', '').split():
    for j in i:
        if j.isdigit() and change_person is False:
            sasha_age += j
            counter += 1
            if counter >= 2:
                change_person = True
        elif j.isdigit() and change_person:
            masha_age += j

print(sasha_age)
print(masha_age)
print(int(sasha_age)+int(masha_age))
