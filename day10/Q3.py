#Q3. Sum to n. Write sum_to(n) that returns 1 + 2 + ... + n. Before running it, draw the call stack on paper for sum_to(4).
def sum_to(n):
    if n == 0:
        return 0
    else:
        return n + sum_to(n - 1)

print(sum_to(4))  
print(sum_to(10))
prompt = int(input("Enter a number to calculate sum_to: "))
print(sum_to(prompt))