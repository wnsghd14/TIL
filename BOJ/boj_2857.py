# lit = [input().split('-') for _ in range(5)]
# # print(lit)
# dic = dict(lit)
# cnt = []
# # print(dic)
import sys
input = sys.stdin.readline

clue = True
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        print(i, end=" ")
        clue = False
if clue == True:
    print("HE GOT AWAY!")