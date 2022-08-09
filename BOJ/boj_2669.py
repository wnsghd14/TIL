# 예시 문제 자료를 잘 보면 1,2,4,4 의 직사각형을 보면 저 네가지수로 사각형을 만들수 있다는 사실을 알수있다.
# 사각형들을 각 각 1X1 로 쪼개면 총 26가지 정사각형이 나오는것을 알수 있었고, 이를 통해 각 점에 값을 대입하여 그 대입 값들을 더하면
# 그 사각형의 면적의 값이겠다는 결론에 도달하였고, 개중 중복값이 있을것을 우려하여 += 1 이아닌 =1로 선언하여 중복값을 차단했다.


xy = [[0 for _ in range(10)] for _ in range(10)]

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
     # 모든 면은 점으로 구성. x,y 의 각 점들의 위치에 1씩을 넣어주어 합하면 결과를 도출할수있다.
    for i in range(x1,x2): # x 축의 값과
        for j in range(y1,y2):# y 축의 값에서
            xy[i][j] = 1 #  인덱스만큼의 점위치에 1을 추가.
    print(xy)
cnt = 0
for k in xy:
    cnt += sum(k)
print(cnt)