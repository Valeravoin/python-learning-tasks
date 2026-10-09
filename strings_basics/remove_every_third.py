# Удаляет символы с индексами, кратными 3 (0, 3, 6, ...)
s = input()
result = ''

for i in range(len(s)):
    if i % 3 != 0:
        result += s[i]

print(result)
