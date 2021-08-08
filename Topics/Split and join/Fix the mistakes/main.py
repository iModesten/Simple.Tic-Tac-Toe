text = input()
words = text.split()
sites = []
for word in words:
    # finish the code here
    if word.lower().startswith('www.') or word.lower().startswith('https:/') or word.lower().startswith('http://'):
        sites.append(word)
print('\n'.join(sites))
