import sys

input = sys.stdin.readline

N = int(input())
sum = 0
data = set()
for i in range(N):
    word = str(input().rstrip())

    if word == "ENTER":
        data.clear()
        continue
    else:
        if word in data:
            continue
        else:
            data.add(word)
            sum += 1

print(sum)