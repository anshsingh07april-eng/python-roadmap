#Q2. Factorial. Write factorial(n) yourself without looking at the example above. Test with 0, 1, 5 and 10.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))  
print(factorial(1))  
print(factorial(5))  
print(factorial(10)) 