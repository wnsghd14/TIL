# 사진 갯수
n = int(input())
# 추천 횟수,추천받은 학생들
m = int(input())
reco = list(map(int, input().split()))

arr = []
cnt = []

for i in range(m):
    if reco[i] in arr:
        idx = arr.index(reco[i])
        cnt[idx] += 1
    else:
        if len(arr) >= n:  # 사진틀이 꽉 찬 경우
            # 추천 받은 횟수가 가장 적은 학생의 사진삭제
            if cnt:
                r = min(cnt)
            for j in range(len(cnt)):
                if cnt[j] == r:
                    arr.pop(j)
                    cnt.pop(j)
                    arr.append(reco[i])
                    cnt.append(1)
                    break
        else:
            arr.append(reco[i])
            cnt.append(1)
    print(arr)
    print(cnt)

arr.sort()
print(*arr)
# enumerate
# (0,1)
# defaultdict
# [{},{}]