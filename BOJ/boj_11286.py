# 18
# 1
# -1
# 0
# 0
# 0
# 1
# 1
# -1
# -1
# 2
# -2
# 0
# 0
# 0
# 0
# 0
# 0
# 0




import heapq

x = int(input())
heap = [] # 힙 리스트 생성
for i in range(x):
    N = int(input()) # 입력받고
    
    if N != 0: # 음수여도 절댓값이기 때문에 0이 아닐때,
        heapq.heappush(heap,(abs(N),N)) # ex -1 을 넣었을때 [1,-1]이런식으로 넣어줌.
    # 사실 모두 한꺼번에 들어가서 될거라 판단하고 구하기 어려웠는데 파이썬튜터가 도움을 줌.
    elif N == 0 and len(heap) == 0:
        print(0) # 0이 연속적으로 나왔을땐 0을 출력하더라구요.
    else: 
        print(heapq.heappop(heap)[1]) # heapq[1] 을 해보았다가 heappop을 쓰면 되겠구나 라고 생각하고 진행 했더니 되었습니다.