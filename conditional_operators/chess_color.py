x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Если суммы координат имеют одинаковую чётность — цвет одинаковый
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print('YES')
else:
    print('NO')
