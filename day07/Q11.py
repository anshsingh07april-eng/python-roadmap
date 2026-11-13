#Q11. Group by length. Given ["hi", "cat", "to", "dog", "apple"], make a dictionary that maps word length to the list of words: {2: ["hi", "to"], 3: ["cat", "dog"], 5: ["apple"]}.
words = ["hi", "cat", "to", "dog", "apple"]
grouped = {}
for word in words:
    length = len(word)
    if length not in grouped:
        grouped[length] = []
    grouped[length].append(word)
print(grouped)