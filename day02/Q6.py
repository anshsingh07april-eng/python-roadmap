#Q6. Palindrome (string version). Check if a word or phrase is a palindrome, ignoring case and spaces (for example, "Never odd or even" is a palindrome). Write it as a function is_palindrome(text) that returns True or False.
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]

sentence = input("Enter a word or phrase: ")
if is_palindrome(sentence):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")