import sys
sys.stdin = open('input.txt')

# board = [0]*100
# A, B, C = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(3)]

# for i in arr:
#     for j in range(i[0]-1, i[1]-1):
#         board[j] += 1
# # print(board)
# sum_ = 0
# for num in board:
#     if num == 1:
#         sum_ += A
#     elif num == 2: 
#         sum_ += 2*B
#     elif num == 3: 
#         sum_ += 3*C
    
# print(sum_)
A,B,C = map(int,input().split())
total = 0
times = [list(map(int,input().split())) for _ in range(3)]
arr = []
away = []
total_val = 0
for i in times:
    away.append(i.pop())
    arr.append(i.pop())

first = [j for j in range(arr[0],away[0])]
second = [j for j in range(arr[1],away[1])]
third = [j for j in range(arr[2],away[2])]
total = [[j,0] for j in range(min(arr),max(away))+1]

for k in total:
    for l in first:
        if k[0] == l:
            k[1] +=1
    for n in second:
        if k[0] == n:
            k[1] +=1
    for m in third:
        if k[0] == m:
            k[1] +=1
print(total)
for x in total:
    # print(total_val)
    if x[1] == 1:
        total_val += A
    elif x[1] == 2:
        total_val += B*2
    elif x[1] == 3:
        total_val += C*3
print(total_val)