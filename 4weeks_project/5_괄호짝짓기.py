import sys

sys.stdin = open("_괄호짝짓기.txt")

# D4 이지만 간단하게 생각했다. 각각의 괄호들이 만난다면 마주친 괄호의 인덱스번호에 있는 괄호를 pop해주자! 계속해서 없애는것이다. 
for tc in range(1,11):
    N = int(input())
    lit = list(input())
    checklist = []
    answer = 1 # 일부러 계속 1로 초기화. 만약 괄호가 더이상 만들어지지 않으면 1로 출력.
    for i in range(N):
        if lit[i] == ")":
            if "(" in checklist:
                checklist.pop(checklist.index("("))
            else : 
                answer = 0
                break
        elif lit[i] == ">" :
            if "<" in checklist:
                checklist.pop(checklist.index("<"))
            else : 
                answer = 0
                break
        elif lit[i] == "}" :
            if "{" in checklist:
                checklist.pop(checklist.index("{"))
            else : 
                answer = 0
                break
        elif lit[i] == "]" :
            if "[" in checklist:
                checklist.pop(checklist.index("["))
            else : 
                answer = 0
                break
        else:
            checklist.append(lit[i])
    print(f'#{tc} {answer}')
            