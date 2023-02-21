def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:   
        answer *= (hash_map[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# 1) HashMap 만들기
# HashMap이란 Key-Value의 Pair를 관리하는 Dictionary이다.
# 이 문제에서 Key는 옷의 종류가 되고, Value는 해당 옷 종류의 가짓수(count)를 의미한다.

# 2) clothes 배열에 존재하는 모든 옷의 종류의 count table 만들기
# 'Hashing을 한다'라고도 표현하는데, HashMap에 의상 종류를 전부 추가해보자. 
# 위 코드의 동작 방식은 다음 예시로 설명하는 것이 가장 쉽게 이해가 가능할 것이다.
# {"headgear" : 2, "eyewear":1}
# Hash Map을 보고 나면 별게 아니다. 이 문제에서는 Key 값으로 전화번호를 관리하는 전화번호부 같은 것이다.
# HashMap.get(type, 0)
# 이 함수는 'B'라는 Key에 해당하는 Value가 있으면 가져오고, 아닐 경우 0을 Default로 지정하여 사용하겠다는 의미의 함수이다.
# Value는 곧 옷 종류의 가짓수가 되기 때문에, 이전에 값이 있었으면 기존 값에 + 1을 하면 되고
# 없었으면 1을 입력하면 된다.
# 3) 각 옷 종류별 경우의 수를 answer에 곱해준다
# 이제 모든 옷 종류의 count가 잘 입력되었다면, answer에 곱해주면 된다.
# 하지만 모든 옷 종류에 대해서 안 입는 경우가 있기 때문에 ans *= it.next().intValue()라고 하지 않고
# ans *= it.next().intValue() + 1을 곱해줘야 한다.
# 즉, +1은 각 옷 종류를 입지 않는 경우를 고려하기 위해 추가되어야 하는 것이다.
# 4) 예외처리
# 아무리 스파이가 모자 하나만 달랑 입어도 된다고 해도, 아무것도 입지 않는 것은 허용되지 않는 것이 문제의 전제이다.
# 그렇기 때문에 마지막에 -1을 해줘서 모든 옷의 종류를 입지 않은 경우 1개를 제외시켜 주고,
# 예제 #2에서도 동일하게 잘 동작하는 걸 확인하면 제출해보고 정답임을 확인할 수 있다.