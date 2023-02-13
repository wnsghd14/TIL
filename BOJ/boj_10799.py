A = input()
ans = 0
ans2 = 0
for a in A:
    if a == "(":
        ans2 += 1
    else:
        ans2 -= 1
        if b == "(": 
            ans += ans2
        else: 
            ans += 1
    b = a
print(ans)


t = list(input())

stack = []
cnt = 0

for i in range(len(t)):
    if t[i] == '(':
        stack.append(t[i])
    else:
        # 레이저
        if t[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
        # 막대기
            cnt += 1
print(cnt)

