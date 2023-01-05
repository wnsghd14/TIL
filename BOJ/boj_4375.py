import sys
input = sys.stdin.readline
# 3 * 37  111
# 7 * 15873  111111
# 9901 * 11222211 111111111111

# 변수를 받을때 많은 양을 받을 수 있기 때문에
# 구글을 찾아봤는데 입력값이 이해가 잘 안된다!
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

for i in arr:
    a = 1 # a 는 1로만 만들어진 숫자이다.
    len = 1 # a의 길이이다
    while a % i != 0: # a 가 i 의 약수가 아니라면
        a += 10**len # a의 자릿수를 늘림
        len += 1 # len을 1 더해준다.
    print(len) # 배수가 되었을때 이때까지 더한 값이 길이이므로 len의 값을 출력한다.