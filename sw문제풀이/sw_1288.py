T = int(input())
# for tc in range(1, T + 1):
    # N = int(input())
#     num = ["0", "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
#     count = 0
    
#     while num:
#         count += 1
#         result = str(N * count) # 

#         for j in result:
#             if j in num:
#                 num.remove(j) # 
#     print('#{} {}'.format(tc, result))
for tc in (1, T + 1):    
    N = int(input())
    N1 = N
    numbers = set()
    # for 반복 : 숫자를 문자로
    # numbers set에 추가
    while True :
        for n in str(N):
            numbers.add(n)
            if len(numbers) == 10:
                break
        # print(n, numbers)
        N += N1
    print(f'#{tc} {N}')