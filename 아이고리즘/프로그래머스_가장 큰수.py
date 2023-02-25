def solution(numbers):
    answer = '' 
    num1 = [str(n)*3 for n in numbers]
    num_list = list(enumerate(num1))
    num_list.sort(key = lambda x:x[1], reverse = True)
    for index, value in num_list:
        answer += str(numbers[index])
        
    return str(int(answer))