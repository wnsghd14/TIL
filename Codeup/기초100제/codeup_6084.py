h,b,c,s = map(int,input().split())
a = round(((h*b*c*s)//8)/1024**2,1)
print(f'{a} MB')