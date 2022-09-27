h,w = map(int,input().split())

arr = [[0]*(w+1) for _ in range(h+1)]

n = int(input())
for i in range(n) :
  l,d,x,y = map(int,input().split())
  
  for j in range(l) :
    if d==0 :
      arr[x][y+j] = 1
    else :
      arr[x+j][y] = 1

for i in range(1, h+1) :
  for j in range(1, w+1) :
    print(arr[i][j], end=' ')
  print()