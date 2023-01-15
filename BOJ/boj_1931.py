# import sys
# input = sys.stdin.readline

# # 회의 시간 리스트
# times = []

# # 회의 개수
# num = int(input())

# # 회의 시간을 튜플로 묶어서 리스트에 저장
# for _ in range(num):
#     times.append(tuple(map(int, input().split())))

# # 시작 시간이 빠른 순서로 정렬 후 종료 시간이 빠른 순서로 정렬
# # 만약 종료 시간이 빠른 순서로만 정렬한다면 시작과 종료 시간이 같은 경우가 앞으로 갈 수 있음
# times.sort()
# times = sorted(times, key=lambda x: x[1])

# # 첫 회의 끝나는 시간
# endTime = times[0][1]

# # 진행되는 회의 수
# cnt = 1

# for idx in range(1, num):
#     # 회의가 시작하는 시간이 이전 회의가 끝나는 시간과 같거나 큰 경우
#     if times[idx][0] >= endTime:
#         # 회의 진행
#         cnt += 1
#         # 회의 끝나는 시간을 업데이트
#         endTime = times[idx][1]
# print(cnt)