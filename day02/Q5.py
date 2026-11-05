#Q5. Vowel counter. Count vowels and consonants in a sentence, ignoring spaces, digits and punctuation. It must work for both uppercase and lowercase letters.
def count_vowels_consonants(sentence):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    return vowel_count, consonant_count 
vsentence = input("Enter a sentence: ")
vowel_count, consonant_count = count_vowels_consonants(vsentence)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")