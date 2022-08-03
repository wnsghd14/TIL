# 처음엔 heapq 을 사용하려고 발악했으나 실패해서 set을 이용하여 간단하게 구하였음.
N,M = map(int,input().split()) # 입력값

A = set(map(int,input().split())) # 입력값을 set에 넣어주면 깔끔해짐
B = set(map(int,input().split())) # 22

print(len(A-B) + len(B-A)) # 결국 길이의 합을 구하는거여서 했습니다.