# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	c=
# ć	c-
# dž dz=
# đ	d-
# lj lj
# nj nj
# š	s=
# ž	z=
# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다.
# lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 
# 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다. 
# 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# ljes=njak, c=c=, dz=ak

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# 6, 3, 2

# 풀이 슬라이싱 한 값을 반목문으로 돌려 input과 비교 의외로 괜찮았다!
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 크로아티아 알파벳
word = input() # 입력값
cnt = 0 # 알파벳의 갯수를 넣어줄 곳
for i in croatia: # 크로아티아알파벳 반복문
    if i in word: # 크로아티아 글자가 있다면
        cnt += word.count(i) # 더해줘라
print(len(word))
print(cnt)
print(len(word)-cnt) # word의 갯수에서 -cnt 갯수를 빼주면 값이 나오드라고요;
        