n = int(input())
tower = list(map(int, input().split()))
tower.reverse()

answer = [0] * n
stack = []
for i, x in enumerate(tower):
    while stack and tower[i] > stack[-1][1]:
        j, y = stack.pop()
        answer[j] = n - i

        if not stack:
            break

    stack.append((i, x))

answer.reverse()
print(*answer)