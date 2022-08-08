T = int(input())
for tc in range(1,T+1):
    lit = list(map(int,input().split()))
    lit.pop(0)
    sor = sorted(lit,reverse=True)
    max_ = 0
    # print(sor)
    # print(sor)
    # print(len(sor))
    for i in range(len(sor)-1):
        max_ = max(max_,sor[i]-sor[i+1])
        # print(max_)
    print(f'Class {tc}')
    print(f'Max {max(sor)}, Min {min(sor)}, Largest gap {max_}')