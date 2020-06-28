
side1 = int(input())
side2 = int(input())
side3 = int(input())
if side1 + side2 + side3 == 180 and side1 == side2 == side3:
    print('equalatieral ')
if side1 + side2 + side3 == 180 and side1 == side2 or side3 == side1 or side3 == side2 and side1 != side2 or side3 != side1 or side3 != side2:
    print('isoceles')

