#Q6. Anagrams. Write is_anagram(a, b) that ignores case and spaces. Then, given a list of words like ["listen", "silent", "enlist", "google", "gogole", "cat", "act"], group the anagrams together using a dictionary and print each group.
def is_anagram(a, b):
    # Normalize the strings: remove spaces and convert to lowercase
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    # Check if the sorted characters of both strings are equal
    return sorted(a) == sorted(b)

words = ["listen", "silent", "enlist", "google", "gogole", "cat", "act"]
anagram_groups = {}

for word in words:
    # Create a normalized key for each word
    key = ''.join(sorted(word.replace(" ", "").lower()))
    # Add the word to its anagram group
    if key not in anagram_groups:
        anagram_groups[key] = []
    anagram_groups[key].append(word)

# Print each group of anagrams
for group in anagram_groups.values():
    if len(group) > 1:  # Only print groups with more than one anagram
        print(group)

is_anagram_result = is_anagram("Listen", "Silent")
print(f"Are 'Listen' and 'Silent' anagrams? {is_anagram_result}")

