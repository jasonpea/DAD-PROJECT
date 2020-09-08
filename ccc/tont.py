t = input()
c = input()
x = []
for i in range(c):
    x.append(input())

w = x.sorted()

sum = 0
count = 0
while count < len(w) and sum <= t:
    sum = sum + w[count]
    count = count + 1
if sum > t:
    print(count - 1)
else:
    print(count)