words = input().split('_')
cap_words = [word.title() for word in words]
print(''.join(cap_words))
