n = [0, 20, 100]
a = 0

for x in n:
    if x >= a:
        a = x

print(a)


# 최댓값 구하기
numbers = [-1, -20, -100, -40]
max_num = float("-inf")
for i in numbers:
    if max_num < i:
        max_num = i

print(max_num)