a,b,c= map(int,input().split())
x = a if a<b else b
y = x if x<c else c
print(y)