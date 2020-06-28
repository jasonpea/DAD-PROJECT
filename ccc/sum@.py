# l = [1,2,3,4,5]
# target = 6
# d = {}
# for index, element in enumerate(l):
#     diff = target - element
#     if diff in d:
#         print([d[diff], index])
#     else:
#         d[element] = index
#
# print(d)
# #NUMBER 1
# s = int(input("please input number: "))
# m = int(input("please input number: "))
# l = int(input("please input number: "))
# if 1 * s + 2 * m + 3 * l > 10:
#     print("Happy")
# else:
#     print("Sad")
#
# p = int(input("please input number: "))
# n = int(input("please input number: "))
# r = int(input("please input number: "))
# w = 0
# i = r
# while i <= p:
#     if r == 1:
#         i += n
#     else:
#         i = r * i
#     w += 1
# print(w)
#
#
#
#
# p = int(input("please input number: ") * 3)
# n = int(input("please input number: ") * 2)
# r = int(input("please input number: ") * 1)
# pp = int(input("please input number: ") * 3)
# nn = int(input("please input number: ") * 2)
# rr = int(input("please input number: ") * 1)
# if p + n + r > pp + nn + rr:
#     print("A")
# elif pp + nn + rr > p + n + r:
#     print("B")
# else:
#     print("T")
# l = int(input('ENTER AN INT: '))
# biglist = []
# #
# # for i in range(l):
# #     w = input()
# #     biglist.append(w)
# #
# # # print(biglist)
#
#
#     # e = str(input())
#
# indices1 = 0
# indices2 = 1
#
# for e in biglist:
#     # print(biglist)
#     c = e.split()
#     # print(c)
#     print(int(c[indices1]) * str(c[indices2]))
# #


#
#

# p = int(input("please input number: "))
# n = int(input("please input number: "))
# r = int(input("please input number: "))
# f = int(input("please input number: "))
# if p == 8 or 9:
#     if r == n:
#         if n == r:
#             if f == 8 or 9:
#                 print("ignore")
#     else:
#         print("answer")


x = int(input("please input number: "))
y = int(input("please input number: "))

if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print("2")
if x and y < 0:
    print("3")
if x > 0 and y < 0:
    print("4")




