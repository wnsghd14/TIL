w = [int(input())for i in range(10)]
k = [int(input())for i in range(10)]
w.sort(reverse=True)
k.sort(reverse=True)
a=w[0]+w[1]+w[2]
b=k[0]+k[1]+k[2]
print(a,b,end=' ')