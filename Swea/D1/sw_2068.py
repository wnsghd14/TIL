T = int(input())

for i in range(T):
    lit = list(map(int, input().split()))
    lit.sort()
    print('#%d' %(i + 1), lit[9])