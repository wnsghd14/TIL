# N = int(input())

# def dp(n):
#     if n <= 1:
#         return [[1, 1], [1, 0]]
#     else:
#         arr = dp(n//2)
#         t0 = arr[0][0]*arr[0][0]+arr[0][1]*arr[1][0]
#         t1 = arr[0][0]*arr[0][1]+arr[0][1]*arr[1][1]
#         t2 = arr[1][0]*arr[0][0]+arr[1][1]*arr[1][0]
#         t3 = arr[1][0]*arr[0][1]+arr[1][1]*arr[1][1]
#         if n%2==0:
#             return [[t0%10007, t1%10007], [t2%10007, t3%10007]]
#         else:
#             arr = [[t0%10007, t1%10007], [t2%10007, t3%10007]]
#             t0 = arr[0][0]+arr[0][1]
#             t1 = arr[0][0]
#             t2 = arr[0][0]
#             t3 = arr[1][0]
#             return [[t0%10007, t1%10007], [t2%10007, t3%10007]]
# print(dp(N)[0][0])


n = int(input())

arr = [0]*n 
#list에 append하는 것보다 0으로 빈 list를 만든 뒤 값을 변경시키는 게 더 편하다
def tyle(n):    
    if n == 1:
        arr[0] = 1
        return 1
    elif n == 2:
        arr[1] = 2
        return 2
    elif arr[n-1] != 0:
        return arr[n-1]
    else:
        arr[n-1] = (tyle(n-1) + tyle(n-2))%10007
        return arr[n-1]

print(tyle(n))