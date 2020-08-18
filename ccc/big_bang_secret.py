k = int(input())
word = input()

newword = ""
for i in range(len(word)):
    letter = word[i]
    # print(letter)
    shift = 3 * (i + 1) + k
    x = ord(letter) - shift
    if x < ord("A"):
        x = ord("Z") + x - ord("A") + 1
    plain = newword + chr(x)

print(newword)
