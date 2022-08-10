a = list(map(int,input().split()))
b = list(map(int,input().split()))
cnt = 0
cnt1 = 0
c = 'D'
for i in range(10):
    if a[i] > b[i] :
        cnt += 3
        c = 'A'
        
    if a[i] < b[i] :
        cnt1 += 3
        c = 'B'
    if a[i] == b[i]:
        cnt += 1
        cnt1 += 1
        
if cnt > cnt1:
    print(cnt,cnt1)
    print('A')
if cnt < cnt1:
    print(cnt,cnt1)
    print('B')
if cnt == cnt1:
    if c == 'A':
        print(cnt,cnt1)
        print('A')
    if c == 'B':
        print(cnt,cnt1)
        print('B')
    if c == 'D':
        print(cnt,cnt1)
        print('D')