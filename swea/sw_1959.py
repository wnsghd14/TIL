T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
 
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
 
    max_result = 0
    if N > M:
        for i in range(N-M+1):
            result = 0
            for j in range(i, M+i):
                result += A[j]*B[j]
 
            if result > max_result:
                max_result = result
            if len(B) == len(A):
                break
            B.insert(0, 0)
 
    elif M > N:
        for j in range(M-N+1):
            result = 0
            for i in range(j, N+j):
                result += A[i]*B[i]
            if result > max_result:
                max_result = result
            if len(B) == len(A):
                break
            A.insert(0, 0)
    else:
        result = 0
        for i in range(N):
            result += A[i]*B[i]
        if result > max_result:
            max_result = result
 
    print(f'#{tc} {max_result}')