t = int(input())
a = list(map(int, input().split()))
count = 0

for i in a: 
    for j in range(2, i+1): # 1은 소수가 아니기 때문에 제외한다!
        if i % j == 0: # 약수중 
            if i == j: # 값이 같다면
                count += 1 # +1해라
            break

print(count)