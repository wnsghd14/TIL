n = int(input())

arr = [0]*n 

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
# DP 점화식
# 피보나치 수열
# n 값이 뽑아주는 갯수의 합을 자꾸 더하면서 나아가는 수열
# 함수형에 익숙해지려 노력중이다.