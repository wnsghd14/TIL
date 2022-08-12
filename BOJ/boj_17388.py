S,K,H = map(int,input().split())
if S+K+H >= 100:
    print('OK')
else:
    lit = [S,K,H]
    x = min(lit)
    if x == S:
        print('Soongsil')
    if x == K:
        print('Korea')
    if x == H:
        print('Hanyang')