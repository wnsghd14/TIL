import sys
input = sys.stdin.readline

arr=[]

while True:
    n = int(input())
    if n==0:
        break
    arr.append(n)

p=list(range(max(arr)))
p[1]=0

for i in range(2,int(len(p)**0.5)+1):
    if p[i]:
        for j in range(2*i,len(p),i):
            p[j]=0

p[2]=0

for i in arr:
    for j in range(len(p)):
        if p[j] and p[i-j]:
            print(i,'=',p[j],'+',p[i-j])
            break

# 일단 모든 인풋값을 받고 시작한다. 해당 인풋값들 중에서 max값을 골라 에라토스테네스의 체를 구현한다.

# 리스트에서 5의 index 값이 5가 되도록 리스트를 만들고, 2부터 루트n까지 순차적으로 쳐낸다. 각각의 배수만 range(,,i) 식으로 방문해서 값을 0으로 만든다.

# 2부터 루트n까지 쳐내는 와중에도 만일 해당 값이 0이라면, 즉 이미 지워졌다면 그냥 패스한다. 이는 에라토스테네스의 체와 동일하다.

# 에라토스테네스의 체로 모두 걸러냈다면 작은 순으로 소수를 찾아가면서 대응되는 수 또한 소수인지 살펴본다. (리스트의 길이가 이론상 1,000,000까지인데, 엄청 빠르게 접근 및 계산이 가능했다. 이는 해당 인덱스의 값에 접근하는 시간복잡도가 O(1)이기 때문이다. 오늘 하나 더 배운다.)

# 만일 두 수가 모두 소수라면 이는 문제에서 요구하는 골드바흐의 추측을 증명한 것이다. 그대로 출력한 뒤 끝낸다.
