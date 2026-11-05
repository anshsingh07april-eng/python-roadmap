#Q4. Word frequency. Take a sentence. Count how many times each word appears using a dictionary (ignore case and punctuation). Print all counts, then the three most frequent words. Do not use collections.Counter for the first version. Afterwards, redo it with Counter and compare.
from collections import Counter
import string

sentence = input("Enter a sentence: ")

sentence = sentence.translate(
    str.maketrans('', '', string.punctuation)
).lower()

words = sentence.split()

word_freq = Counter(words)

print("Word frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

print("\nThree most frequent words:")
for word, freq in word_freq.most_common(3):
    print(f"{word}: {freq}")