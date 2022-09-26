n, m = map(int,input().split())
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다. 
c = (n if n >=m else m)
print(c)