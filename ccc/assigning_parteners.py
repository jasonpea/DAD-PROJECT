
n = int(input())

first1 = input().split()
second2 = input().split()

i = 0
status = "good"
while i < n and status == "good":
    position = first1.index(second2[i])
    if first1[i] != second2[position] or position == i:
        state = "bad"
    i += 1

print(status)