n = int(input())

cnt = 1
start_num = 0
while True:
  start_num += cnt
  cnt += 1
  if start_num >= n:
    break
print(start_num)