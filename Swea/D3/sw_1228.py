import sys

sys.stdin = open('./Swea/D3/1228.txt','r')

for tc in range(1, 11):

    n = int(input())

    result_num = list(input().split())

    k = int(input())

    num = list(input().split())


    while len(num):
        num.pop(0)
        idx = int(num.pop(0))
        length = num.pop(0)


        for i in range(int(length)):
            result_num.insert(idx+i, num.pop(0))
        




    print('#{} {}'.format(tc, ' '.join(result_num[:10])))