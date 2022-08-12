from collections import deque
queue = deque()
while True:
    n = input()
    if n == '고무오리 디버깅 시작':
        continue
    if n == '고무오리 디버깅 끝':
        break
    if n == '문제':
        queue.append(n)
    if n == '고무오리':
        if len(queue) ==0:
            queue.append('문제')
            queue.append('문제')
        else:
            queue.pop()
print(queue)
if queue:
    print('힝구')
else:
    print('고무오리야 사랑해')