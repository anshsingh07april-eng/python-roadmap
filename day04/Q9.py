#Q9. Count vowels. Write count_vowels(text) that returns the number of vowels in a sentence, for both capital and small letters.
sentence = input("Enter a sentence: ")
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
print(f"Number of vowels: {count_vowels(sentence)}")