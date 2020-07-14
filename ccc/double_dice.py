antonia = 100
david = 100

howmanyr = int(input())

for i in range(howmanyr):
    roll = input().split()
    a = int(roll[0])
    d = int(roll[1])
    if a < d:
        antonia = antonia - d
    elif d < a:
        david = david - a
print(antonia)
print(david)


