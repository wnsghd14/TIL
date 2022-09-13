import sys

sys.stdin = open("_암호문1.txt")


for i in range(10):
    n = int(input())
    original_list = list(input().split())
    orderCount = int(input())
    order = input().split('I')
    order_list = []
 
    for j in order:
        tmp = list(j.split())
        order_list.append(tmp)
 
    print(tmp)
