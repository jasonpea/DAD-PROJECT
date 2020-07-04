# starred = '*'
# x = 'x'
# double_x = 'xx'
# space = ' '
# scale = int(input())
# output = []
# counter = 0
# for i in range(scale):
#     #output.append(starred * scale + x * scale + starred * scale)
#     print(starred * scale + x * scale + starred * scale)
#     # counter += 1
#     # if counter == scale:
#     #     print((space * scale + double_x * scale)*scale)
# for i in range(scale):
#     print(space * scale + double_x * scale)
# for i in range(scale):
#     print(starred * scale + space * scale + starred * scale)
#
#
#
#
#
#
#
















"""
*x*
 xx
* *
"""
num = int(input("input number less then 25: "))
for i in range(num):
    print("*"*num+"x"*num+"*"*num)
for i in range(int(num)):
    print("{}{}{}".format(" "*num, "x"*num, "x"*num))
for i in range(int(num)):
    print("{}{}{}".format("*"*num, " "*num, "*"*num))








