n = int(input())
lit = list(map(int,input().split()))
m = int(input())
lit1 = list(map(int,input().split()))
dic = {}
for i in lit:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for i in lit1:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')