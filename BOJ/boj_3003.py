list_ = [1,1,2,2,2,8]


T = list(map(int,input().split()))

for i in range(6):
    print(list_[i]-T[i],end=' ')

