# N,M = map(int,input().split())
# lit = []
# li = [input() for _ in range(N)]
# met = [input() for _ in range(M)]
# # print(li,met)
# for i in range(len(li)):
#     for j in range(len(met)):
#         if li[i] == met[j]:
#             lit.append(li[i])
#             lit.sort()
# print(len(lit))
# for k in lit:
    # print(k)
N,M = map(int,input().split())
lit = set()
lit1 =set()
for _ in range(N):
    lit.add(input())
for _ in range(M):
    lit1.add(input())
lit2 = list(lit & lit1)
lit2.sort()
# print(lit,lit1)
print(len(lit2))
for k in lit2:
    print(k)