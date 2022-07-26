# A, B = map(int, input().split())

# for i in range(min(A, B), 0 , -1):  ### 최대공약수 구하기.
#     if A % i == 0 and B % i == 0:  ###가장 작은수 부터 1까지 -1을 하며  
#         print(i) # 만약 a%i b%i 값이 모두 떨어져서 
#         break # 나머지가없을때 i 는 최대공약수이다.
# for i in range(max(A , B), (A * B) + 1): ### 최소공배수 구하기
#     if i % A == 0 and i % B == 0: ### 가장 큰 수 부터 두 변수를 곱한 값까지
#         print(i) ### 의 수를 반복, 배수들 중 공통을 찾아 
#         break ### i % A and i% B 가 나머지가 없을때 최소공배수
# 위가 원래 나의 풀이. 하지만 시간초과로 실패하였다.



## 유클리드 호제법을 사용.
## 유클리드 호제법이란.
## a와 b의 최대공약수 == b와 r(a % b의값)의 최대공약수
## a = 10 b = 12
## 10 % 12 == 10
## 12 % 10 == 2
## 10 % 2 == 0
A, B = map(int, input().split())

def GCD(A, B): # 최대공약수
     while B > 0: # => A % B != 0
         A, B = B, A % B
     return A
def LCM(A, B): # 최소공배수
    result = (A * B) // GCD(A, B)
    return result
 # 최소공배수는 A * B 를 최대공약수로 나눈 몫 이다.

print(GCD(A, B))
print(LCM(A, B))