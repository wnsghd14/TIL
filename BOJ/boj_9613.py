# 최소공배수의 합을 구하는 프로그램을 작성한다.
# 우선 최소공배수를 구하는 함수를 짠 후에
# 3중포문을 통해 리스트내에있는 각 값들을 일일히 비교하여 그값들의 최소공배수를 정답을위한 total에 넣으며 일일히 비교하였다.
def GCD(a, b):
     
    if a >= b :
        if a%b == 0:
            return b
        else:
            while a%b != 0:
                if (a%b != 0) and (b != 0) :
                    c = a%b
                    a = b
                    b = c            
                else : c = b
            return b

    if a < b :
        if b%a == 0:
            return a
        else:
            while b%a != 0:
                if (b%a != 0) and (a != 0) :
                    c = b%a
                    b = a
                    a = c            
                else : c = a
            return a
    
N = int(input())

for i in range(0, N):
    A = list(map(int, input().split()))
    B = []
    for i in range(1, len(A)-1):
        for j in range(i+1, len(A)):
            c = GCD(A[i], A[j])
            B.append(c)
    print(sum(B))

# 유클리드 호제법을 이용하는 간단한 문제.
# 유클리드 호제법은 간단히 말해서 두 수의 나머지를 이용하여
# 최대 공약수를 찾아나가는 방법임
# import sys
# input = sys.stdin.readline
# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)

# T = int(input())
# for _ in range(T):
#     arr = list(map(int,input().split()))
#     total = 0
#     for i in range(1,len(arr)):
#         for j in range(1,len(arr)):
#             if i < j:
#                 total += gcd(arr[i],arr[j])
#             else:
#                 pass
#     print(total)
