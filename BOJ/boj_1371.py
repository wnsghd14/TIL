# import sys
eng = 'abcdefghijklmnopqrstuvwxyz'
result = []
# inp = sys.stdin.read()
input_ = input()
for i in eng:
    result.append(input_.count(i))

m = max(result)
for j in range(len(result)):
    if m == result[j]:
        print(chr(j+97), end = '')