# 55
# 5 5 10
# 5 0  5  # 3
# 0 5 5
# 5 5 10
# lit = []
# lit1 = []
# for i in input():
#     lit.append(i)
# 20 + 6    
# n = int(input())
# m =(n%10)*10 + (n//10 + n%10)
# print(26//10+ 26%10)
# print(26%10) def 써서 했어도 될거같다.; 구현귀찮.
n = int(input())
x = n
cnt = 0
while 1:
    sum_ = n % 10 + n // 10
    new_ = n%10*10 + sum_%10
    cnt += 1

    n = new_
    if new_ == x:
        break
print(cnt)