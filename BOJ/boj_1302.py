N = int(input())
dic = dict()
lit = []
for i in range(N):
    book = input()
    if book not in dic:
        dic[book] = 1
    else:
        dic[book] += 1
    # print(dic)

for j in dic:
    if max(dic.values()) == dic[j]:
        lit.append(j)
lit.sort()
print(lit[0])