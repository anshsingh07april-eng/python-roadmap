#Q7. Word count. Take a sentence and count each word (ignore capital letters). Print the counts and the most frequent word.
sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:", word_count)
print("Most frequent word:", max(word_count, key=word_count.get))