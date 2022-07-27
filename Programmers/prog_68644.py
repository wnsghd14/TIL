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


def solution(numbers):
    answer = []
    set_ = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]

            sum_ = n1 + n2

            set_.add(sum_)
    answer = sorted(list(set_))
    return answer