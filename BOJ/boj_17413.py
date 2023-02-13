arr = list(input())
n = False
word1 = ''
word2 = ''
for i in arr:
    if n == False:
        if i == '<':
            n = True
            word1 = word1 + i
        elif i == ' ':
            word1 = word1 + i
            word2 = word2 + word1
            word1 = ''
        else:
            word1 = i + word1
    elif n == True:
        word1 = word1 + i
        if i == '>':
            n = False
            word2 = word2 + word1
            word1 = ''
print(word2+word1)