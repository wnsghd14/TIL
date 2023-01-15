s = str(input())

cnt = 0
cnt1 = 0

temp = s[0]
# 첫번째 인덱스값 확인
if temp == "1":
    cnt += 1
else:
    cnt1 += 1
# 맨앞 인덱스 제외한 나머지 검사
for i in range(1,len(s)):
    if temp != s[i]:
        if s[i] == "1":
            cnt += 1
            temp = s[i]
        else :
            cnt1 += 1
            temp = s[i]
# 그중 큰값 뽑으면 답임

if cnt >= cnt1:
    print(cnt1)
else:
    print(cnt)