

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split(" "))))


if l[0][0] > l[0][1]:
    if l[0][0] > l[1][0]:
        rotationsNeeded = 2
    else:
        rotationsNeeded = 3
else:
    if l[0][0] < l[1][0]:
        rotationsNeeded = 0
    else:
        rotationsNeeded = 1


for i in range(rotationsNeeded):
    lTemp = []
    for j in range(n):
        rowTemp = []
        for k in reversed(l):
            rowTemp.append(k[j])
        lTemp.append(rowTemp)
    l = lTemp


for i in l:
    st = ""
    for j in range(n):
        st += str(i[j]) + " "
    print(st[:-1])