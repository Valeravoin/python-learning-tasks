# Выводит индекс второго вхождения буквы «f»
# -2 — если нет ни одного, -1 — если только одно
s = input()

first = s.find('f')

if first == -1:
    print(-2)
else:
    second = s.find('f', first + 1)
    if second == -1:
        print(-1)
    else:
        print(second)
