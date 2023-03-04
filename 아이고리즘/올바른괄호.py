# s = "()()"
# s = "(())()"
# s = ")()("
s = "(()("
stack = []
answer = True
for i in s:
    if i == '(':
        stack.append(i)
    else:
        if stack == []:
            answer = False
        else:
            stack.pop()
if stack != []:
    answer = False
print(answer)