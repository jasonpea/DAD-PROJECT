t1 = int(input())
t2 = int(input())

count = 2
while t1 >= t2 >= 0 and t1 >= 0:
    count += 1
    t3 = t1 - t2
    t1 = t2
    t2 = t3
print(count)
