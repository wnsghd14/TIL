N = [int(input())for i in range(3)]
if sum(N) == 180:
    if N[0]==N[1]==N[2]:
        print('Equilateral')
    elif N[0] == N[1] or N[1] == N[2] or N[2] == N[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')