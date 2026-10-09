s = input()
last_digit = s[-1]

count_3 = 0
count_last = 0
count_even = 0
sum_big = 0
prod_big = 1
count_05 = 0

for char in s:
    digit = int(char)

    if digit == 3:
        count_3 += 1

    if char == last_digit:
        count_last += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_big += digit

    if digit > 7:
        prod_big *= digit

    if digit == 0 or digit == 5:
        count_05 += 1

print(count_3)
print(count_last)
print(count_even)
print(sum_big)
print(prod_big)
print(count_05)
