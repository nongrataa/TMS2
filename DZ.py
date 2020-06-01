#ввести сумму и вывести 3 рубля 45 копеек

a = float(input("input a -  "))
k = (a % 1)*100
#print(k)
r = a - (a % 1)
if k == 0 :
    print(f"{int(r)} рубля")
else:
    print(f"{int(r)} рублей, {int(k)} копеек")


