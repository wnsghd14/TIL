import sys

sys.stdin = open('./Swea/D3/1225.txt','r')

for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
#마지막 자리수가 0이 될때까지 반복시작
    while arr[-1] > 0:
#5번 돌아가는것이 1사이클이므로 for문으로 5번씩 돌려준다
        for i in range(1, 6):
#arr[0]이 i 보다 작거나 같으면 0으로 만들어서 맨 뒤로 보내고 끝낸다
            if arr[0] <= i:
                arr.append(0)
                arr.pop(0)
                break
#arr[0]이 i보다 크면 i만큼 빼고 뒤로 보내서 다시 돌린다
            else:
                arr.append(arr[0] - i)
                arr.pop(0)
    print(f"#{tc} ",end = '')
    print(*arr)