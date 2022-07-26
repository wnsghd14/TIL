score = []  # 리스트 만들고

for i in range(5): # 5명이 참가함
    score.append(sum(map(int, input().split()))) # 리스트에 더한 값을 넣어줌

print(score.index(max(score))+ 1, max(score)) # 리스트의 인덱스는0부터 시작.
                                              # 1더해주고 최댓값까지 출력.