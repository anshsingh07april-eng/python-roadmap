#Q7. Unique words. Take a sentence from the user and print how many different words it has, ignoring case.
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")