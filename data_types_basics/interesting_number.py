n = int(input())

if 100 <= n <= 999:
    # Получаем цифры
    d1 = n // 100          # сотни
    d2 = (n // 10) % 10   # десятки
    d3 = n % 10           # единицы

    digits = [d1, d2, d3]
    digits.sort()         # теперь: [min, mid, max]
    minimum, middle, maximum = digits[0], digits[1], digits[2]

    if maximum - minimum == middle:
        print('Число интересное')
    else:
        print('Число неинтересное')
else:
    print('Число не трёхзначное')
