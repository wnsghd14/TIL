while True:
    N = input()
    if N == '#':
        break
    value = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = 0
    for i in range(len(N)):
        if N[i] in value:
            result += 1
    print(result)