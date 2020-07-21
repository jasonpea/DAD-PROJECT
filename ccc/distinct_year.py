
year = int(input()) + 1
def distinct(year):
    s = str(year)
    for digit in s:
        if s.count(digit) > 1:
            return False
    return True
while not distinct(year):
    year = year + 1

print(year)

