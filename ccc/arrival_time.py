h, m = input().split(":")
h, m = int(h), int(m)

distanceTime = 0.0

while distanceTime < 120:
    m += 1

    if 6 < h < 10:
        distanceTime += 0.5
    elif 14 < h < 19:
        distanceTime += 0.5
    else:
        distanceTime += 1

    if m == 60:
        if h == 23:
            h = 0
        else:
            h += 1
        m = 0


if m < 10:
    if h < 10:
        print("0" + str(h) + ":" + "0" + str(m))
    else:
        print(str(h) + ":" + "0" + str(m))
else:
    if h < 10:
        print("0" + str(h) + ":" + str(m))
    else:
        print(str(h) + ":" + str(m))
#all my dad knows is 'get up early' meanwhile he himself gets up at like 9:00
#then he says 'while doing homework you can't get up to drink water or pee' im thinking ya
#the only reason why u don't have to fucking drink water is becuz u have a whole jug of it right beside u lazy ass
#my 'dad' is cringe af and i hate him
#and he says while doing homework u can't watch youtube or anything well why don't u not watch tik tok???? and when i catch
#you, you make excuses to cringe ass. he's legit on his phone for at least like 60 percent of the time he's over there 'working'
#im never gonna do anything for him ever again as long as it's not needed. So that means i'm never gonna make food for him
#and if mom tells 'ME' to do anything i'll tell dad to do it since he's older and he's supposed to be doing more chores
#and his excuse for no doing chores is 'OOHHHHHi need to studyyyy' like omfg why didn't u studyyyyy when u were 20 and not when ur frickin 45 years
#old, like goddamn ur just making me and mom and daniel do alll the work while u sit there every single day doing who knows wut
#cringe ass, study study well u study'd enough did u not?????? and u still fucking failed a test wow ur a disgrace.
#gosh why am i the only kid that has a iresponsible dad that thinks he know everything, like OHHHH PLAY THE PIAON FOR 50 MIN
#ya why don't u sit there and do something productive without fucking picking up that filthy iphone of yours and watching 30 min of tik tok??
#all he does is abuse his power as a dad, like i wake up early and he says i have to stop watching youtube by 9:00
#then he get's proved wrong and tries to fucking waste all my goddamn time like ohhhh go BRUSH YOUR TEETH AND CHANGE YOUR CLOTHS
#he thinks he's so cool. And he's a fricking snake too.
#and i bet the next time we go to china he's gonna tell all our relatives that ohh i don't do anything or he'll tell them i do alot
# and act all proud and gratefull, meanwhile at home he cuts me zero fucking slack, like goddamn i don't even have to do any house chores
#right now, daniel didn't do any, like fuck, i've done more in 10 years than dad has done his entire life, and when he's taking a class
#he need me or my mom or daniel to fucking feed him to his stiniky ass fucking mouth and all he has to do is sit there and wait
#he always says 'OH I HAVE WORK TO DO, ITS URGENT' ya well tell me this, why the fuck does it take u from 9:30 in the morning to fucking 8 o'clock
#u are supposedly working 11 hours a fucking day and getting zero over pay that OR you aren't working at all and just wasting time watching tik tok
# and SAYING and being cringe and telling daniel 'OH IM WORKING' like we all know your work is easy af and can be done so easily 