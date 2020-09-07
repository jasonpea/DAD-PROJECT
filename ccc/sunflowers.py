n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split(" "))))


if l[0][0] > l[0][1]:
    if l[0][0] > l[1][0]:
        rotationsneeded = 2
    else:
        rotationsneeded = 3
else:
    if l[0][0] < l[1][0]:
        rotationsneeded = 0
    else:
        rotationsneeded = 1


for i in range(rotationsneeded):
    lTemp = []
    for j in range(n):
        rowtemp = []
        for k in reversed(l):
            rowtemp.append(k[j])
        lTemp.append(rowtemp)
    l = lTemp


for i in l:
    st = ""
    for j in range(n):
        st += str(i[j]) + " "
    print(st[:-1])