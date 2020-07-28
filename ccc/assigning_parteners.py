
n = int(input())

first = input().split()
second = input().split()

# for each position i, it must be the case that
# first [i] = second[position in first of second[i]]
# (ie. a to b is also b to a)
# and that position in first of second[i] not = i
# (ie. a to a is not the case)

i = 0
state = "good"
while i < n and state == "good":
    position = first.index(second[i])
    if first[i] != second[position] or position == i:
        state = "bad"
    i = i + 1

print(state)