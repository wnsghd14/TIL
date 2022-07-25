md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())

for i in range(T):
    N = input()
    month = int(N[4:6])
    day = int(N[6:8])
    res = "-1"
    if 1<=month and month<=12 and 1<=day and day<=md[month-1]:
        res = N[0:4]+"/"+N[4:6]+"/"+N[6:8]
    print(f"#{i+1} {res}")