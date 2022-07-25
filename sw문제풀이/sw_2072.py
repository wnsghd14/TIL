T = int(input())
for tc in range(T) :
    nums = map(int,input().split())
    res = sum(n for n in nums if n%2==1)
    print( f"#{tc+1} {res}" )