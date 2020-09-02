startPoint = list(map(int, input().split(" ")))
endPoint = list(map(int, input().split(" ")))


batteryPower = int(input())


distance = ((startPoint[0] - endPoint[0]) + (startPoint[1] - endPoint[1]))
if batteryPower < distance:
    print('N')
else:
    if (batteryPower - distance) % 2 == 0:
        print("Y")
    else:
        print("N")
