startpoint = list(map(int, input().split(" ")))
endpoint = list(map(int, input().split(" ")))


batteryPower = int(input())


distance = ((startpoint[0] - endpoint[0]) + (startpoint[1] - endpoint[1]))
if batteryPower < distance:
    print('N')
else:
    if (batteryPower - distance) % 2 == 0:
        print("Y")
    else:
        print("N")
