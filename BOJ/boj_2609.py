A, B = map(int, input().split())
small = min(A, B)
large = max(A, B)
# 최대 공약수
## 최대 공약수는 둘 중 작은 값보다 작다
for i in range(small,0,-1):
    if small %i != 0 :
        continue
    if large % i == 0:
        print(i)
        break

#최소 공배수
## 최소 공배수는 둘 중 큰 값보다 크다
i = 0
while True:
    i+=1
    temp = large * i
    if temp % small == 0:
        print(temp)
        break


# 유클리드 호제법
# 유클리드 호제법이란.
# a와 b의 최대공약수 == b와 r(a % b의값)의 최대공약수
# a = 10 b = 12
# 10 % 12 == 10
# 12 % 10 == 2
# 10 % 2 == 0
# 
# A, B = map(int, input().split())

# def GCD(A, B): # 최대공약수
#     while B > 0: # => A % B != 0
#         A, B = B, A % B
#     return A
# def LCM(A, B): # 최소공배수
#     result = (A * B) // GCD(A, B)
#     return result
#  # 최소공배수는 A * B 를 최대공약수로 나눈 몫 이다.

# print(GCD(A, B))
# print(LCM(A, B))