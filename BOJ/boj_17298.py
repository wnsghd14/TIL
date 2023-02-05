import sys
input = sys.stdin.readline
N = int(input())

num = list(map(int,input().split()))
check = [0] * N
check[N-1] = -1
#print(check)

for i in range(N-2,-1,-1):
    if num[i] < num[i+1]:
        check[i] = num[i+1]
    else:
        if check[i+1] > num[i]:
            check[i] = check[i+1]
        elif check[i+1] == -1 :
            check[i] = -1
        else:
            check[i] = -1
            for j in range(i+1,N):
                if check[j] > num[i]:
                    check[i] = check[j]
                    break
                elif check[j] == -1:
                    break
for j in check:
    print(j, end=' ')