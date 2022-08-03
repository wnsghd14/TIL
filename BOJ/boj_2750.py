N = int(input())
list_ = [] # set으로 접근하려다 머리가 너무 복잡해져서 리스트사용
for i in range(N):
    t = int(input()) # 
    list_.append(t)
list_.sort()

for j in list_: # 각각 리스트 내부의 값들을 나눈뒤 하나씩 출력.
    print(j)
