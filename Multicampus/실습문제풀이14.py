# word = 'apple'
cnt = 0
word = list(input())
for i in range(len(word)):
    if word[i] == 'a':
        cnt += 1
    
print(cnt)

word2 = 'applea'
count = 0
for char in word2:
    if char == 'a':
        count += 1

print(count)