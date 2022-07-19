# str
numbers = int(input())

answer = 0

for i in str(numbers):
	answer += int(i)

print(answer)

# while
number = 123
result = 0
while number:
	result += number % 10
	number //= 10

print(result)
# divmod 
# divmod(x,y) 는 x를 y로 나누고, 결과를 tuple 로 변환
number1 = 123
results = 0

while number1 :
	results, remainder =divmod(number1, 10)
	results += remainder

print(results)