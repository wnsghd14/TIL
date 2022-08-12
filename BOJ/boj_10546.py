N = int(input())
dic = dict()
for i in range(2*N-1):
    maratoner = input()
    if maratoner not in dic:
        dic[maratoner] = 1
    else:
        dic[maratoner] += 1
print(dic)
for k,v in dic.items():
    if v % 2 ==1:
        print(k)