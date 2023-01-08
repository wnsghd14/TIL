import sys
input = sys.stdin.readline
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    total = 0
    for i in range(1,len(arr)):
        for j in range(1,len(arr)):
            if i < j:
                total += gcd(arr[i],arr[j])
            else:
                pass
    print(total)