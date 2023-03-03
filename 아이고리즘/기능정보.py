progresses = [93, 30, 55]
speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
answer = []
while progresses :
    cnt = 0
    while progresses and progresses[0] >= 100:
        cnt+=1
        progresses.pop(0)
        speeds.pop(0)
    progresses = [progresses[i]+speeds[i] for i in range(len(progresses))]
    if cnt:
        answer.append(cnt)
print(answer)
