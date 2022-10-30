a = int(input())
answer = []
for i in range(a):
    b,c = map(int,input().split())
    result = b+c
    answer.append(result)
for j in answer:
    print(j)