s1 = input().split()
s2 = input().split()

result = []

for i in range(len(s1)):
    result.append(int(s1[i]) + int(s2[i]))

print(*result)
