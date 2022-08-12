import sys

sys.stdin = open("_Flatten.txt")

for i in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    while dump:
        max_box = max(box) # 최댓값과
        min_box = min(box) # 최솟값에서
        max_idx = box.index(max(box)) # 최댓값의 인덱스를 찾고
        min_idx = box.index(min(box)) # 최솟값의 인덱스를 찾는다.
        box[max_idx] -= 1 # 평탄화 과정 
        box[min_idx] += 1 # 평탄화 과정
        dump -= 1

    print(f'#{i} {max(box)-min(box)}')