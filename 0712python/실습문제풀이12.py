word = 'apple'
new_word = ""

for i in word:
    if i == 'a':
        continue
    else:
        new_word += i
print(new_word)