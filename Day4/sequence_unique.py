"""Нужно проверить, все ли числа в последовательности уникальны."""
my_list = [1, 3, 4, 5, 2, 6, 13, 7, 12, 9]
count2 = 0
count = 0
for i in my_list:
    count2 = count
    count = 0
    for j in my_list:
        if i == j:
            print(i)
            count += 1
            print('count - ', count)

print('count2', count2)
if count2 >= 2:
    print("Последовательность не уникальна")
else:
    print('Последовательность уникальна')
print()
