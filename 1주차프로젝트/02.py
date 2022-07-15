with open('fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    
cnt = text.split('\n')

list = set()

for name in cnt:
    if name.endswith('berry'):
        list.add(name)
# print(list)
# print(len(list))
with open('02.txt', 'w', encoding='utf-8') as f:
    f.write(f'{len(list)}\n')
    for i in range(len(list)):
        f.write(f'{list.pop()}\n')

