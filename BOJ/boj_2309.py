lit = [int(input()) for _ in range(9)]
total = sum(lit)

for i in range(9):
    for j in range(i+1, 9):
        if total -  100 == (lit[i] + lit[j]):
            x=lit[i]
            y=lit[j]     # 여기서 lit[i] lit[j] 를 remove해줄수가 없다.
lit.remove(x)            # 왜나면 index에 에러가 생김. 여러숫자를 빼내기때문에.
lit.remove(y)
lit.sort()
for i in lit:
    print(i)
# 그냥 간단하게 풀었다. 리스트에서 이중포문을 만들어 list의 합에서 100을 뺀값이
# 각 for 문에서 뽑은 값의 합과 같다면 x,y 로 선언후 그값을 리스트내에서 빼주고
# 오름차순으로 정리하는것이다. 그러고 그 리스트를 출력하면 끝.