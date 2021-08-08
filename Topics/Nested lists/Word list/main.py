text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
len_of_word = int(input())
list_of_words = [word for words in text for word in words if len(word) <= len_of_word]
print(list_of_words)
