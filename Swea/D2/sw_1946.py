T = int(input())
for i in range(1, T+1):
    N = int(input())
    text = ''
    for n in range(N):
        alpa, num = input().split()
        text += alpa*int(num)
    print(f'#{i}')
    print(text)
    for i in range(0,len(text),10): # 0부터 10의 간격으로 len(text)-1 까지의 정수
        print(text[i:i+10]) # [i] 에서 부터 [i+10] 까지의 값을 출력한다