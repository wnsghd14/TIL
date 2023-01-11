s = str(input())

count_one = 0
count_zero = 0

temp = s[0]
# 첫번째 인덱스값 확인
if temp == "1":
    count_one += 1
else:
    count_zero += 1
# 맨앞 인덱스 제외한 나머지 검사
for i in range(1,len(s)):
    if temp != s[i]:
        if s[i] == "1":
            count_one += 1
            temp = s[i]
        else :
            count_zero += 1
            temp = s[i]
# 그중 큰값 뽑으면 답임

if count_one >= count_zero:
    print(count_zero)
else:
    print(count_one)