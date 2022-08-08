N = int(input())
b = '* '
for i in range(1,N+1):
    print(b*N)
    if i % 2 == 1:
        print(' ',end='')