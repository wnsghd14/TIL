T = int(input())

for i in range(1, 1+T):
    A, B = map(int, input().split())
    N = A + B
    print(f'Case #{i}: {N}')
