a = []

for i in range(1, 1001):
    if i < 99:
        a.append([i, 0])
    elif 98 < i < 801:
        a.append([i, i * .25])
    else:
        a.append([i, 200])

print(a)

for i in a:
    print(i[1])
    