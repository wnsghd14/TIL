# N = int(input())
# arr = []
# for i in range(N):
#     T = int(input())
#     arr.append(T)
#     arr.sort()
# arr1 = []
# arr2 = []
# for j in range(len(arr)):
#     if len(arr) > 1:
#         arr1.append(min(arr))
#         arr.pop(0)
#         arr2.append(max(arr))
#         arr.pop(-1)
#     else:
#         if len(arr1) > len(arr2):
#             arr2.append(arr)
#         else:
#             arr1.append(arr)
#     print(arr1)
#     print(arr2)

import sys
input = sys.stdin.readline

n = int(input())

card = []
count = 0

for i in range(n):
    card.append(int(input()))

card.sort()

for i in range(n-1): # 작은거두개
    card[i+1] = card[i] + card[i+1]
    count += card[i+1]

    for j in range(i+1, n-1): # 큰거 
        if card[j] > card[j+1]:
            card[j], card[j+1] = card[j+1], card[j]

        else:
            break

print(count)