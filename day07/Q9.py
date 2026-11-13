#Q9. First non-repeating character. For the word swiss, find the first letter that appears only once (answer: w). Use your counts from Q6.
word = "swiss"
char_count = {}
for char in word:
    char_count[char] = char_count.get(char, 0) + 1
for char in word:
    if char_count[char] == 1:
        print(f"The first non-repeating character in '{word}' is: {char}")
        break
else:
    print(f"No non-repeating character found in '{word}'.")