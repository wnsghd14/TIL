n = int(input())
plus = []
minus = []
zero = 0
one = 0
for i in range(n):
    x = int(input())
    if x == 1:
        one += 1
    elif x > 0:
        plus.append(x)
    elif x < 0:
        minus.append(x)
    else:
        zero += 1

plus.sort(reverse = True)
minus.sort()
if len(plus)%2 == 1:
    plus.append(1)
if len(minus)%2 == 1:
    if zero > 0:
        minus.append(0)
    else:
        minus.append(1)
ans = one
for i in range(0,len(plus),2):
    ans += plus[i]*plus[i+1]
for i in range(0,len(minus),2):
    ans += minus[i]*minus[i+1]
print(ans)