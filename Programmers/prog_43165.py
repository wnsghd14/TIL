# numbers = [1,1,1,1,1]
# target = 3
numbers = [4,1,2,1]
target = 4
answer = 0
leaves = [0]
for i in numbers:
    temp = []
    for j in leaves:
        temp.append(j + i)
        temp.append(j - i)
    leaves = temp
for k in leaves:
    if k == target:
        answer += 1
print(answer)