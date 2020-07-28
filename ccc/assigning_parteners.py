
n = int(input())

first = input().split()
second = input().split()

i = 0
status = "good"
while i < n and status == "good":
    position = first.index(second[i])
    if first[i] != second[position] or position == i:
        state = "bad"
    i += 1

print(status)