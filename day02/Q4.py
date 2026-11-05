#Q4. String report. Take a sentence from the user and print: its length, the uppercase version, the lowercase version, the title-case version, the number of words, and the sentence with spaces replaced by hyphens.
sentence = input("Enter a sentence: ")

print(f"Length: {len(sentence)}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title-case: {sentence.title()}")
print(f"Number of words: {len(sentence.split())}")
print(f"Hyphenated: {sentence.replace(' ', '-')}")