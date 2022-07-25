T = int(input())

lst = list(map(int, input().split()))
lst.sort()
print(lst[int((T - 1) / 2)])