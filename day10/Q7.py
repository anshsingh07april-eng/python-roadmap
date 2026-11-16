#Q7. Palindrome. Write is_palindrome(s) that returns True or False. Compare the first and last letters; if they match, check the middle part. Test with "madam", "racecar" and "hello".
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

palindrome_tests = ["madam", "racecar", "hello", "A man, a plan, a canal: Panama", "No 'x' in Nixon"]
for test in palindrome_tests:
    result = is_palindrome(test)
    print(f"Is '{test}' a palindrome? {result}")