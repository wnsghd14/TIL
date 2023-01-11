# n은 동전의 종류, k는 만들어야 할 금액
n, k = map(int, input().split()) 
a = []
m = 0

# 동전의 종류 n개 리스트로 정렬
for i in range(n) : 
    a.append(int(input()))

a.sort(reverse=True)

# k를 a[j]로 나눈 몫을 더함 
# k는 k를 a[j]로 나눈 나머지  
for j in range(n) :
    if k - a[j] >= 0 :    
        m += k // a[j]    
        k = k % a[j]      
    if k == 0 :
        break    
        
print(m)