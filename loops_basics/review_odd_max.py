count = 0
maximum = None

for _ in range(4):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if maximum is None or x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')
