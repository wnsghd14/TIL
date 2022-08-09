lit = []
for i in range(5):
    N = int(input())
    lit.append(N)
    lit.sort()
    sum_ = sum(lit)
print(int(sum_ / 5))
print(lit[2])
