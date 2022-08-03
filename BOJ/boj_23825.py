# 문제
# 당신은 SASA 연못에서 알파벳 S 모양의 블록 $N$개와 알파벳 A 모양의 블록 $M$개를 건졌다. 태영이는 연못에서 건진 블록을 이용해 학교에 전시할 SASA 모형을 최대한 많이 만들려고 한다.

# SASA 모형 $1$개를 만들기 위해서는, 알파벳 S 모양의 블록 $2$개와 알파벳 A 모양의 블록 $2$개가 필요하다. 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 구하라.

# 입력
# 첫째 줄에 알파벳 S 모양의 블록의 개수 $N$과 알파벳 A 모양의 블록의 개수 $M$이 공백으로 구분되어 주어진다.

# 출력
# 태영이가 만들 수 있는 SASA 모형 개수의 최댓값을 출력한다.

# 제한
#  $1 \leq N, M \leq 10^9$ 
# 예제 입력 1 
# 4 5
# 예제 출력 1 
# 2

N, M = map(int, input().split()) 

print(min(N//2,M//2)) # 4 와 6 이런식일때 어차피 두개밖에 안되서 최솟값을 생각했다.
