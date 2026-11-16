#Q14. Permutations. Print all arrangements of the letters in "abc" (there are 6).
def print_permutations(s, current_permutation):
    if len(s) == 0:
        print(current_permutation)
        return

    for i in range(len(s)):
        next_permutation = current_permutation + s[i]
        remaining_letters = s[:i] + s[i+1:]
        print_permutations(remaining_letters, next_permutation)
        break
    
prompt = input("Enter a string of letters: ")
print("All permutations of the string are:")
print_permutations(prompt, "")