T = int(input())
end = 666
cnt = 1
while cnt != T: # 1일땐 바로 출력하게끔. cnt 값이 T에 도달하지 못할때 까지 
    end += 1 # w
    if '666' in str(end):
        cnt += 1 # T에 도달할때 까지 더해줘야함.
print(end)
# 문제해석이 첫번째
# for 문으로 단순히 접근했다가 실패를 여러번하고
# 문제를 다시읽었더니 1일때는 666 2일때는 1666 이다.
# cnt 가 2가 아닐때 더한다는 소리는 2일때 까지 end에 더해준다는 소리임.
# 그렇다면 666을 가진 다음 수는 1666 이 되는것이다.
# 예시로 10개를 input 했을때
# 666,1666(cnt+=1),2666(cnt+=1),3666(..),4666,5666,6660,6661,6662,6663
# 이 되기 때문에 6663이 프린트가 되는 형식이다.