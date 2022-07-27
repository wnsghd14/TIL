# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 
# 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# Mississipi, zZa, z

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# ?, Z, z

# 나의 풀이
# 딕셔너리
alpha = input().upper() # 대문자로변경
dict_alpha = {} # 빈 딕셔너리 생성
result = 0 # 결과
count = 0 # 횟수
# 딕셔너리에 값 넣는 반복문
for i in alpha: # 입력받은 문자 반복
    if i in dict_alpha: # 반복해서 담긴 문자열 
        dict_alpha[i] += 1 # 더하기
    else:
        dict_alpha[i] = 1 # 없으면 1
# print(dict_alpha[i])
# print(i)

# 담겨있는 입력값 수 검증하는 반복문
for j in dict_alpha: # 입력값 담겨있는 상태의 dict 반복하여
    if dict_alpha[j] > count: # 횟수보다 크다면
        count = dict_alpha[j] # 횟수 변수에 저장
        result = j # 결과값
    if dict_alpha[j] == count: # 같다면
        result = '?' # ? 출력

print(result)

# list, coun와 index 함수를 이용한 풀이
# word = input().upper()
# word_list = list(set(word))
# lst = []

# for i in word_list:
#     count = word.count(i)
#     lst.append(count)

# if lst.count(max(lst)) >= 2:
#     print("?")
# else:
#     print(word_list[lst.index(max(lst))])



