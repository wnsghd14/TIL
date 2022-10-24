a,b = map(int,input().split())

if a != 0:
    if b - 45 < 0:
        result1 = a - 1
        result2 = b+60-45
    else:
        result1 = a
        result2 = b - 45
else:
    if b -45 < 0:
        result1 = 24 - 1
        result2 = b +60 - 45
    else:
        result1 = a
        result2 = b - 45
print(result1,result2)