# 크기가 N인 파스칼의 삼각형을 만들어야 한다.

# 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.

# 1. 첫 번째 줄은 항상 숫자 1이다.

# 2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.

# N이 4일 경우,
 



# N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.


# [제약 사항]

# 파스칼의 삼각형의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스에는 N이 주어진다.


# [출력]

# 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.

# 삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 삼각형 배열을 먼저 만드는것을 구글링 해봤음. 대충 인덱스로 만든다고 보고
# 행렬에서 윗값과 왼쪽윗값을 더한값을 result에 넣으면 되겠구나 하고 길게 짜다가 실패
# 구글링 해서 ..풀었는데 이해는 완벽.
import sys
sys.stdin = open('./Swea/input.txt','r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = [[1]*i for i in range(1,N+1)] #처음에 1로 다 채워주기 삼각형을 만들어야 하니깐~
    for i in range(N):
      if i > 1: # 1보다 클 때만
        for j in range(1, len(num[i])-1): #맨 처음이랑 맨 마지막 범위를 제외하고
          num[i][j] = num[i-1][j] + num[i-1][j-1]  #위 값+ 왼쪽 위 값
    print(f"#{tc}")
    for i in range(N):
        print(*num[i])