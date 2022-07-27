N = int(input()) 
way_list = list(map(int, input().split()))
hill_way = 0 # 오르막길
longest = [] #길이

for i in range(N - 1):
    if way_list[i] < way_list[i + 1]: # 오르막길이라면
        hill_way += way_list[i + 1] - way_list[i] # 큰값에서 작은값을 빼

    if way_list[i] >= way_list[i + 1]: ##else 쓰지말라심 
        hill_way = 0 
longest.append(hill_way) # 여기 넣어줍니다.
print(max(longest))# 가장 큰 값을 출력

N = int(input())
sum_ = 0
sum_list = []

list_ = list(map(int,input().split()))

for i in range(1,len(list_)):
    if list_[i] > list_[i-1]:
        sum_ = sum_ + list_[i] - list_[i-1]
        sum_.append(sum_)
    else:
        sum_ = 0
sum_.append(sum_)

if len(sum_list) == 0:
    print(0)
print(max(sum_list))