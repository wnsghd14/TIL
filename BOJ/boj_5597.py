import sys
input = sys.stdin.readline
temp = [i for i in range(1,31)]
# print(temp)
for i in range(1,29):
    n = int(input())
    temp.remove(n)
print(min(temp))
print(max(temp))
