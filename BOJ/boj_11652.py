# N= int(input())
# dic =dict()
# lit = list()
# for _ in range(N):
#     T = int(input())
#     if T not in dic:
#         dic[T] = 1
#     else:
#         dic[T] += 1
# print(dic)
# for j in dic:
#     if max(dic.values()) == dic[j]:
#         lit.append(j)
# print(min(lit))
N= int(input())
dic =dict()
lit = list()
for _ in range(N):
    T = int(input())
    if dic.get(T):
        dic[T] += 1
    else:
        dic[T] = 1
# print(dic)
lit1 = sorted(dic.items())
for k,v in lit1:
    if max_ < v:
        max_ = v
        result = k
print(result)
# import heapq


# N = int(input())

# counts = {}

# queue = []

# for _ in range(N):
#     card = int(input())

#     if card not in counts:
#         counts[card] = 0
    
#     counts[card] += 1

#     heapq.heappush(queue, (-counts[card], card))

# priority, card = heapq.heappop(queue)

# print(card)
