N, M = map(int,input().split())
result = True
for i in range(M):
    k = int(input())
    lst = list(map(int,input().split()))
    # print(lst)
    if lst != sorted(lst, reverse = True):
        result = False
    
if result == True:
    print('Yes')
else:
    print('No')
