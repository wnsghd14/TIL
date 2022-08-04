import sys
input = sys.stdin.readline

x = [int(input()) for _ in range(10)]
print(int(sum(x)/10))
y =list(set(x))
z = []
for i in range(len(y)):
    z.append(x.count(y[i]))
print(y[z.index(max(z))])
    
