num_ = set(range(1,10001))
num_1 = set()

for i in range(len(num_)):
    for j in str(i):
        i += int(j)
    num_1.add(i)

num_2 = sorted(num_ - num_1)
for i in num_2:
    print(i)
    