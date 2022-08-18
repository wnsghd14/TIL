
# 우리편 야스오(피카츄, 아구몬, ...)
# yasuo_1_hp = 100
# 상대편 야스오(버터풀, 야도란, ...)
# yasuo_2_hp = 100
# # nope!
# class Yasuo:

#     def __init__(self):
#         self.health = 100
#         self.energy = 0


# yasuo1 = Yasuo()
# yasuo2 = Yasuo()
# yasuo1.health = yasuo1.health - 20
# yasuo1 = 80, yasuo2.health = 100

import random


def generate_lotto(n):
    result = []
    for i in range(5):
        numbers = range(1, 46)
        pick = random.sample(numbers, 6)
        pick.sort()
        result.append(pick)
    return result

print(generate_lotto(5))