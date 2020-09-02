def ispalindrome(word):
    if word == word[::-1]:
        return True
    return False


w = input()


count = 1
# print(len(w))
for i in range(len(w)):
    # print(count)
    # print(i)
    for j in range(len(w) - 1, i, -1):
        if ispalindrome(w[i:j+1]):
            if j+1-i > count:
                count = j+1-i
print(count)