# star_rectangle.py
height = 4
width = 17

print('*' * width)
for _ in range(height - 2):
    print('*' + ' ' * (width - 2) + '*')
print('*' * width)
