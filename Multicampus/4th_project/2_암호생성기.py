import sys

sys.stdin = open("_암호생성기.txt")

# 이건 뎈 써야겠다 생각 하다 리스트로 풀어버림.
# 리스트에서 pop해준 값과 일정한 범위내에서 반복하는 cnt 값을 빼다보면 0이나 음수가 될때 리스트의 끝에 0 을 넣은후 그 값을 출력하는 구조를 짜보았다.
# 값이 매우 커 손으로 직접 해본결과 각 숫자의 1의자리수에다 10을 더해준값에서 아래의 과정을 했더니 되길래 거기서 정답을 찾을때 도움을 얻음.
for t in range(1, 11):
    tc = int(input())
    queue = list(map(int, input().split()))  
    cnt = 1
    while True:# 꽤나 큰수가 즐비하기때문에 while문을 사용하였다.
        if cnt > 5: # 밑에서 맨앞의 숫자에서 cnt 만큼을 빼줄텐데 그 수가 5를 넘어가면 리셋이 되었기때문에
            cnt = 1 # 다시 리셋을 한다.
        num = queue.pop(0) - cnt # 맨앞의 수를 cnt회차()만큼 뺀값을 선언.
        if num <= 0: # 만약 맨앞의 수에서 몇회차 cnt를 뺄때 그값이 음수이거나 0 일때는 맨뒤를 0으로 치환하며 암호를 생성하기때문에
            queue.append(0) # 음수값이 표에 나오는것을 방지할수 있다.
            break
        queue.append(num) #
        cnt += 1

    print(f'#{tc}',*queue)

    # 도움을 받은 구글답.

# for _ in range(10):
#     # 테스트 케이스 번호
#     tc = int(input())
#     # 8개의 데이터
#     arr=list(map(int,input().split()))

#     # 마지막이 0이 나올때까지 반복
#     while arr[-1] > 0:
#         # 사이클 1~5
#         for i in range(1,6):
#             # 뺀 값을 마지막에 추가하고 원래 값은 삭제
#             # 빼서 0보다 작으면 0으로 바꿔서 넣기
#             if arr[0]-i > 0:
#                 arr.append(arr[0]-i)
#                 arr.pop(0)
#             else:
#                 arr.append(0)
#                 arr.pop(0)
#                 break

#     print(f'#{tc}',*arr)
