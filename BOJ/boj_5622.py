# 전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

# 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

# 상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

# 할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

# 출력
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

# 예제 입력 1 
# WA
# 예제 출력 1 
# 13
# 예제 입력 2 
# UNUCIC
# 예제 출력 2 
# 36
# 나의 풀이.
# 간단하게 하나씩하면 쉽게 풀겠네~ 라곤 했다. 하지만 더 좋은방법이 있더라..
N = input()
cnt = 0
for i in N:
    if i == 'A' or i == 'B' or i == 'C':
        cnt += 3
    elif i == 'D' or i == 'E' or i == 'F':
        cnt += 4
    elif i == 'G' or i == 'H' or i == 'I':
        cnt += 5
    elif i == 'J' or i == 'K' or i =='L':
        cnt += 6
    elif i == 'M' or i =='N' or i =='O':
        cnt += 7
    elif i == 'P' or i =='Q' or i =='R' or i =='S':
        cnt += 8
    elif i == 'T' or i =='U' or i =='V':
        cnt += 9
    elif i == 'W' or i =='X' or i =='Y' or i =='Z':
        cnt += 10
    else:
        cnt += 0
print(cnt)

## 인덱스함수 이용 어제 준혁님의 설명에서 본걸 적용한건 아니고, 찾음;
## 담엔 꼭 써먹어야지
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = input()
result = 0 # 구할값 0으로 초기화
for i in range(len(alpha)): # str국룰
    for j in dial: # 리스트 내부 값을 한번더 반복해 0~7까지로
        if alpha[i] in j:
            result += 3 + dial.index(j) # 1이 2번 이기 때문에0부터 시작한 인덱스에 3 더해줌.
print(result)
        