file = input()

city = list(map(int, file.split(" ")))

# for i in city:
#     if i == ' ':
#         city.append()
#     else:
#         city.append(i)
#
#
#



print(0, city[0], city[0]+city[1], city[0]+city[1]+city[2], city[0]+city[1]+city[2]+city[3])
print(city[0], 0, city[1], city[1]+city[2], city[1]+city[2]+city[3])
print(city[0]+city[1], city[1], 0, city[2], city[2]+city[3])
print(city[0]+city[1]+city[2], city[1]+city[2], city[2], 0, city[3])
print(city[0]+city[1]+city[2]+city[3], city[1]+city[2]+city[3], city[2]+city[3], city[3], 0)





