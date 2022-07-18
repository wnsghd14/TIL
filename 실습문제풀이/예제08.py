# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)
# or 연산은 하나라도 참이면 항상 참이다.
# 그렇기 때문에 항상 참이되어 word의 갯수를 세게 된다.
# 일일히 char == 을 붙여주면 되겠지만 in 함수를 활용하는것이 더 좋은 방법이다.
word = "HappyHacking"

count = 0

for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1
        

print(count)