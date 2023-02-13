bracket = list(input())

stack = []
answer = 0
cnt = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        cnt *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        cnt *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += cnt
        stack.pop()
        cnt //= 2 
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += cnt

        stack.pop()
        cnt //= 3

if stack:
    print(0)
else:
    print(answer)