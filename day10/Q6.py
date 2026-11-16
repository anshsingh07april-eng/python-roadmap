#Q6. Reverse a string. Write reverse_string(s) using recursion.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")