# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# 입력
# 첫째 줄에 구간의 시작과 끝을 나타내는 정수 A, B(1 ≤ A ≤ B ≤ 1,000)가 주어진다. 즉, 수열에서 A번째 숫자부터 B번째 숫자까지 합을 구하면 된다.

# 출력
# 첫 줄에 구간에 속하는 숫자의 합을 출력한다.

# 예제 입력 1 
# 3 7
# 예제 출력 1 
# 15

# 33/3444/4555556666667777777 인건지
# 3/456/7 인지 알수가없네; 
# 풀이 
# 요것도 맞네 ;
# M,N = map(int, input().split()) # 입력값 받고
# list_ = [] # 리스트 생성
# for i in range(N+1): # 반복문 7까지니까
#     #print(i)  # 0 1 2 3 4 5 6 7
#     for j in range(i): # 위 숫자들 하나씩 더해줘
#         list_.append(i)
#         #print(list_)
#         if N == len(list_): # 7까지 갔을때 멈춰
#             break
#         #print(list_)
# set_list_ = set(list_)

# print(sum(list_[M-1:N]))

# 풀이
M,N = map(int, input().split()) # 입력값 받고
list_ = [] # 리스트 생성
for i in range(N+1): # 반복문 7까지니까
    #print(i)  # 0 1 2 3 4 5 6 7
    for j in range(i): # 위 숫자들 하나씩 더해줘
        list_.append(i)
        #print(list_)
        if N == len(list_): # 7까지 갔을때 멈춰
            break
        #print(list_)
print(sum(list_[M-1:N])) # 0부터 니까 M-1