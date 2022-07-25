# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")
a = int(input())
b = int(input())  # 각 input 값 준비
c = int(input())
T = a * b * c    
num_list = list(str(T))   # 곱한값을 스트링으로 형변환
for i in range(10): # 0~9 까지의 숫자에서 가짓수만 출력
    print(num_list.count(str(i)))