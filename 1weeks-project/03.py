with open('fruits.txt', 'r', encoding='utf-8') as f:
    fruit = list(f.read().split('\n'))

dict = {}
for i in fruit:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

# for i in dict:
#     print(i, dict[i])

with open('03.txt', 'w', encoding='utf-8') as a:
    for k, v in dict.items():
        a.write(str(k)+'')
        a.write(str(v)+'\n')