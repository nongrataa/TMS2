data = "sasha 43sdf, masha 23"
correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cheker = False
age = ''

for i in data:
    if i.isdigit():
        age += i
sasha_age = int(age[0:2])
masha_age = int(age[2:4])
print(sasha_age+ masha_age)
