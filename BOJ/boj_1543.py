word_list = list(input())
word = input()
tmp = ''
cnt = 0
for i in word_list:
    tmp += i
    # print(tmp)
    if word in tmp:
        cnt +=1
        tmp = ''
print(cnt)
# 리스트로 아예 받아서 리스트 내의 글자를 하나씩 가져와서 넣고
# 해당글자가 있으면 초기화 하는식으로 구현. 
# abababa 를 뜯어보면 aba, aba 이런식인데 만약 cnt 에 1이 더해졌을때 그값이 초기화 되어
# i+3 부터 시작한 (aba)'b'aba 'b'  부터 시작한다.