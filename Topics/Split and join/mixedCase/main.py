words = input().split()
upper_words = [word.title() for word in words]
upper_words[0] = upper_words[0].lower()
print(''.join(upper_words))
