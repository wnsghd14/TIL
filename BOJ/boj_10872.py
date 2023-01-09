# 간단하게 모든 숫자값을 포문돌려 리스트에넣고 리스트안의 값을 곱해주었다.

T = int(input())
arr = []
for i in range(1,T+1):
    arr.append(i)

ans = 1
for n in arr:
    ans *= n
print(ans)
