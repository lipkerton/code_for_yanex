with open('dataset_3380_5.txt') as inf:
    f = []
    for line in inf:
        line = line.lower().split('\t')
        f += [line]
a = dict()
b = []
for i in range(len(f)):
    for j in range(len(f[i])):
        f[i][j] = f[i][j].replace('\n', '')
        a[f[i][0]] = []
for i in range(len(f)):
    for j in range(len(f[i])):
        a[f[i][0]] += [int(f[i][2])]
for key, value in a.items():
    a[key] = round(sum(value)/len(value), 5)
    if a[key] == []:
        a[key] == '-'
for key, value in a.items():
    b += [[(int(key)), value]]
b = sorted(b)
for i in range(len(b)):
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
    print()
with open('наконец-то все.txt', 'w') as ouf:
    for i in range(len(b)):
        for j in range(len(b[i])):
            ouf.write(f'{b[i][j]} ')
        ouf.write('\n')
