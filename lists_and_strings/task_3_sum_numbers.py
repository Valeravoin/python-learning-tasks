s = input().split()
numbers = []

for i in s:
    numbers.append(int(i))

result = sum(numbers)

print(f"{'+'.join(s)}={result}")
