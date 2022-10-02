import sys

sys.stdin = open('./Swea/D3/1216.txt', 'r')

for tc in range(10):
  N = int(input())
  characters = [list(input()) for _ in range(100)]
  characters2 = list(map(list, zip(*characters)))
  cnt = 100
  found = False
  
  while cnt <= 100:
    for i in range(100-cnt+1):
      for j in range(100-cnt+1):
        if characters[i][j:j+cnt] == characters[i][j:j+cnt][::-1]:
          found = True
        if characters2[i][j:j+cnt] == characters2[i][j:j+cnt][::-1]:
          found = True
    if found == True:
      break
    cnt -= 1
  print(f"#{N} {cnt}")







# # 주어진 단어가 회문 구조인지 확인


# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# # 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기


# def find_palindrome(row, max_length):
#     # 100글자부터 2글자까지 슬라이딩
#     for length in range(100, max_length - 1, -1):
#         # print(length)
#         for c in range(0, (100 - length) + 1):
#             # print(c, len(row[c : c + length]))
#             if is_palindrome(row[c: c + length]):
#                 return length
#     return 1


# T = 10
# for _ in range(1, T + 1):
#     test_case = int(input())
#     max_palindrome = 1  # 가장 긴 회문의 길이

#     # 100 x 100 크기의 글자판 입력받아 2차원 리스트로 구현
#     matrix = [input() for _ in range(100)]

#     # 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기
#     for row in matrix:
#         length = find_palindrome(row, max_palindrome)
#         max_palindrome = max(max_palindrome, length)

#     # 글자판 행렬 뒤집기
#     new_matrix = [[None] * 100 for _ in range(100)]
#     for c in range(100):
#         for r in range(100):
#             new_matrix[c][r] = matrix[r][c]

#     # 글자판의 열을 순회하면서 가장 긴 회문의 길이 찾기
#     for row in new_matrix:
#         length = find_palindrome(row, max_palindrome)
#         max_palindrome = max(max_palindrome, length)

#     print(f"#{test_case} {max_palindrome}")
