words = input().split()

new_word = [word[1:] + word[0] + 'ки' for word in words]

result = ' '.join(new_word)
print(result)
