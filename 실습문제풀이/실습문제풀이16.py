word = input()
cnt = 0
for i in word:
    if i in 'aeiou':
        cnt += 1
   
print(cnt)