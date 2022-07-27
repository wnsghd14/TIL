# 어떤 정수들이 있습니다. 
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

# 나의 풀이.
def solution(absolutes, signs): 
    answer = 0 # answer를 absol 안의 int 값을 받아줄 변수로 선언.
    
    for i in range(len(absolutes)): # int니까
        if signs[i] == True: # 말. 그대롭니다.
            answer += absolutes[i] # 양수를 넣어준다.
        else: # == if signs[i] == False:
            answer -= absolutes[i] # 음수를 더하여 준다.
    return answer # 더해준값을 나타내!

    
# 어느 고수님들의 풀이
# def solution(absolutes, signs):
#     for i in range(len(absolutes)):
#         if signs[i] == False:
#             absolutes[i] = -absolutes[i]
#     return sum(absolutes) 근처까지 갔었는데 sum을 깜빡...
#
# def solution(absolutes, signs): # 진짜 pythonic
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs)) # zip 도 알게됨.
