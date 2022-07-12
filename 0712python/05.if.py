# 값 초기화
# n = 0
# total = 0
# user_input 값
user_input = int(input())
# 처음 시작 값
n = 0
# 0부터 더하기 위해서
result = 0

while n <= user_input:
    result += n
    n += 1
print(result)