import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for tc in range(1,T+1):
    n = input()
    cnt = [0]*101 
    max = 0 
    grade = 0 
    arr = list(map(int,input().split())) 
    for i in range(len(arr)):
        cnt[arr[i]] += 1
    for j in range(1,len(cnt)):
        if max <= cnt[j]:
            max = cnt[j]
            grade = j
 
    print('#{} {}'.format(tc, grade))