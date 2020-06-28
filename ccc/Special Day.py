month = int(input())
day = int(input())
if month < 2 and day < 18:
    print('before')
if month <= 2 and day > 18:
    print("after")
if month <= 2 and day < 18:
    print("before")
if month < 2 :
    print('before')
if month > 2:
    print('after')
if month == 2 and day == 18:
    print('special day')