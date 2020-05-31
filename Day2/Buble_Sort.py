data = [4, 3, 5, 2, 6, 7, 4, 3, 2, 34, 66]
data2 = []

for i in range(len(data) - 1):
    print('i - ',i)
    print(data[i])
    f = 0
    for j in range(len(data)-i-1):
        print('j - ', j)
        print(data[j])
        if data[j] > data[j + 1]:
            data2 = data[j]
            data[j] = data[j + 1]
            data[j + 1] = data2
            f = 1
    if f == 0:
        break

print(data)

