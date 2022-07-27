with open('fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
cnt = text.split('\n')

for i in range(len(cnt)):
    i += 1
print(i)

with open('01.txt', 'w', encoding='utf-8') as f:
    f.write(str(i))