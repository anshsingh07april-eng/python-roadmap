#Q6. Character count. Take a word and print how many times each letter appears, like {'b': 1, 'a': 3, 'n': 2} for banana.
word = "banana"
char_count = {}

for char in word:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)