w_and_l = []
w = 0
l = 0


for i in range(6):
    w_and_l.append(str(input("enter w or l:")))
# print(w_and_l)
for o in w_and_l:
    if o == 'w':
        w += 1


if w == 5 or w == 6:
    print(1)
if w == 3 or w == 4:
    print(2)
if w == 1 or w == 2:
    print(3)
if w == 0:
    print(-1)





