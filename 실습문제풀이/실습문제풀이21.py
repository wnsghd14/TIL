# while 문 사용
numbers = int(input())
answer = 0

while numbers != 0:
    i = numbers % 10
    answer = (answer * 10) + i
    numbers = numbers // 10
print(answer)

# def 정리
n = int(input())

def f(n):
    if n <= 0 : return
    print(n % 10, end = '')
    f(n//10)

f(n)   

# math 사용
from math import log10

num = int(input())
numlist = []
case = int(log10(num))+1
for i in range(case-1, -1, -1):
    numlist.append(num // 10**i)
    num -= ((num // 10**i) * 10**i)

for j in range(len(numlist)-1, -1, -1) :
    print(numlist[j], end='')

# str 사용
number = 123

print(int(str(number)[::-1]))