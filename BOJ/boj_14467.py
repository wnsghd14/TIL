# N = int(input())
# lit = []
# lit1 = []
# result = []
# for i in range(N):
#     cow = list(map(int,input().split()))
#     # print(cow_num)
#     if cow[1] == 1:
#         lit.append(cow[0])
#     elif cow[1] == 0:
#         lit1.append(cow[0])
# x=lit+lit1
# print(x)
# dic = {}
# for j in x:
#     try:
#         dic[j] += 1
#     except:
#         dic[j] = 1
#     print(dic)
# for k, v in dic.items():
#     if v >= 2:
#         result.append(k)
# print(len(result))
# 하 개킹받네

n = int(input())
dic = {}
cnt = 0
for i in range(n):
    cow,cross = map(int, input().split())
    if cow not in dic: 
        dic[cow] = cross
    else: 
        if dic[cow] != cross:
            cnt += 1
            dic[cow] = cross
print(cnt)
