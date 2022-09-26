T = int(input())
a = ['3', '6', '9'] # 리스트로 접근
for i in range(1, T +1):
    count = 0
    for j in str(i):
        if j in a:
            count += 1
    if count > 0:   # 이 구문이 사실상 핵심.
        i = '-' * count  
    print(i, end = ' ')