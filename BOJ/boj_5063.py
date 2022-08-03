T = int(input())

for i in range(T):
    r,e,c = map(int,input().split()) 
    t = e - c # 순 이익이 광고하지않았을때의 수익보다 높아야 해서 비교를 위해
    if r < t:
        print('advertise')
    elif r == t:
        print('does not matter')
    else:
        print('do not advertise')
