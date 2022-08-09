numbers = [0, 20, 100, 40]
max_num = numbers[0]
sec_num = numbers[0]

for n in numbers:
    if max_num < n:
        #최대값이었던 것이 두번째로 큰수
        sec_num = max_num
        max_num = n
    elif sec_num < n and n < max_num:
        sec_num = n
print(sec_num)
