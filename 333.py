data = "sasha 43sdf, masha 23"
age = ''
name=''
name_sasha = ''
name_masha = ''
for i in data:
    if i.isdigit():
        age += i
    else:
        name += i
    if i.is == '':
        name_sasha=name

print(name)
#name = name.replace(',', '').split()
print(name)
print(age)

print(name_sasha)
print(name_masha)
sasha_age = int(age[0:2])
masha_age = int(age[2:4])
print(sasha_age + masha_age)
