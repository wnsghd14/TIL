N = int(input())

for i in range(N):
    M = input()
    lst = list(M)
    sum = 0
    
    for i in lst:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0: # 음수일때.
            print('NO')
    if sum > 0: # 0보다 크면 괄호가 VPS 가 안님
        print('NO')
    elif sum == 0: # 0 일때는 똑같.
        print('YES')