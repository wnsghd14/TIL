# 사진 틀 갯수
n = int(input())
# 추천 횟수, 추천받은 학생들
m = int(input())
recomm = list(map(int, input().split()))

frame = []
cnt = []

for i in range(m):
    if recomm[i] in frame:
        idx = frame.index(recomm[i])
        cnt[idx] += 1
    else:
        if len(frame) >= n:  # 사진틀이 꽉 찬 경우
            # 추천 받은 횟수가 가장 적은 학생의 사진 삭제
            if cnt:
                r = min(cnt)
            for j in range(len(cnt)):
                if cnt[j] == r:
                    frame.pop(j)
                    cnt.pop(j)
                    frame.append(recomm[i])
                    cnt.append(1)
                    break
        else:
            frame.append(recomm[i])
            cnt.append(1)
    print(frame)
    print(cnt)

frame = sorted(frame)
print(*frame)