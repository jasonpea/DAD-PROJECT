t = int(input())
c = int(input())

x = []
for i in range(c):
    x.append(int(input()))

a = sorted(x)

summ = 0
count = 0
while count < len(a) and summ <= t:
    summ += a[count]
    count += 1
if summ > t:
    print(count - 1)
else:
    print(count)