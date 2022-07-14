word = input()
result = ''
for char in word:
    number = ord(char)
    number = number - 32
    result += chr(number)

print(result)