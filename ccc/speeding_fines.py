speedinglimit = int(input())
speedcar = int(input())
if speedcar <= speedinglimit:
    print("congrats ur fine")
elif speedcar > speedinglimit:
    if speedcar - speedinglimit <= 20:
        print("You are speeding and your fine is $100.")
    if speedcar - speedinglimit <= 30 and speedcar - speedinglimit > 20 :
        print("You are speeding and your fine is $270.")
    if speedcar - speedinglimit >= 31:
        print("You are speeding and your fine is $500.")



