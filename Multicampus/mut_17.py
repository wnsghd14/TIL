###
z = 'banana'

result = {}
for char in z:
    if not char in result:
        result[char] = 1
    else:
        result[char] += 1

print(result)

###
word = 'banana'

a = {}

for i in word:
    a[i] = a.get(i, 0) + 1
print(a)

for key in result:
    print(key, result[key])