T = int(input())

for test_case in range(1, T + 1):
    if T % test_case == 0:
        print(test_case, end = ' ')