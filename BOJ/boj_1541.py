import sys

input = sys.stdin.readline().rstrip()
num = ''
arr = []

for i in range(len(input)):
    if input[i] == '+' or input[i] == '-':
        arr.append(num)
        arr.append(input[i])
        num = ''
        continue
        
    num += input[i]
    
    if i == len(input) - 1:
        arr.append(num)


print(arr)
    
for i in range(len(arr)):
    
    if arr[i] == '+':
        continue
    
    if arr[i] == '-':
        for j in range(i + 1, len(arr)):
            if arr[j] == '-' :
                break
                
            if arr[j] == '+':
                arr[j] = '-'

print(arr)

result = int(arr[0])
for i in range(1, len(arr)):
    if i % 2 != 0:
        continue
    if i % 2 == 0 and arr[i - 1] == '+':
        result += int(arr[i])
    elif i % 2 == 0 and arr[i - 1] == '-':
        result -= int(arr[i])
        
print(result)


# exp = input().split('-') #'-'를 기준으로 split해서 exp 리스트에 저장

# num = [] #'-'로 나눈 항들의 합을 저장할 리스트

# for i in exp:
#     sum = 0
#     tmp = i.split('+') #덧셈을 하기 위해서 '+'를 기준으로 split
#     for j in tmp: #split한 리스트의 각 요소들을 더해줌
#         sum += int(j)
#     num.append(sum) #각 항의 연산 결과(덧셈)를 num에 저장

# n = num[0] #식의 제일 처음은 숫자로 시작하기 때문에 0번째 값에서 나머지 값들을 빼준다

# for i in range(1,len(num)): #1번째 값부터 n에서 빼준다
#     n -= num[i]
# print(n)