# 똑같이 모든 숫자를 꺼내어 리스트에 저장후 값을 곱한값을 문자열로 만든후 거꾸로 돌려 0이 없을때 브레이크를 걸어주었다!

T = int(input())
arr = []
for i in range(1,T+1):
    arr.append(i)

ans = 1
for n in arr:
    ans *= n
cnt = 0
for i in str(ans)[::-1]:
    if i != '0':
       break
    cnt += 1
print(cnt)
