import sys
sys.stdin = open('input.txt')

T = int(input())
lit = []
lit1 = []
for i in range(T):
    A,B = input().split()
    lit.append(sorted(A))
    lit1.append(sorted(B))
# print(lit,lit1)
    if lit[i] == lit1[i]:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')