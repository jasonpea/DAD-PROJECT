


max = int(input("Max patient: "))  # reach the number
source_patient = int(input())  # day 0
rate = int(input())  # rate
day = 0
current_patient = source_patient * rate
while current_patient <= max:
    if rate == 1:
        current_patient = current_patient + source_patient
    else:
        current_patient = current_patient * rate
    day += 1
    if current_patient > max:
        print(day)
