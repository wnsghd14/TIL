from pprint import pprint
arr = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num += list(map(int, input().split()))
# pprint(arr)
# pprint(num)
answer = [0] * 12
b_count = 0
count = 0

for i in range(len(num)):
    count += 1
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if num[i] == arr[y][x]:
                answer[x] += 1
                answer[y+5] += 1
                if x == y:
                    answer[10] += 1
                if x+y == 4:
                    answer[11] += 1

    for j in range(len(answer)):
        if answer[j] == 5:
            answer[j] = 0
            b_count += 1

    if b_count >= 3:
        break
    
print(count)
