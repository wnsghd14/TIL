# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)): # 이중반복문 사용.
        for j in range(len(numbers)):
            if i != j:  # 같지 않을때 더해준다!
                answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer))) #set 하고 sort 해준다.
print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
