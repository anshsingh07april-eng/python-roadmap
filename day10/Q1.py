#Q1. Countdown. Write countdown(n) that prints n, n-1, ... 1 and then Go!. Do not use a loop.
def countdown(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        countdown(n - 1)
prompt = int(input("Enter a number to start countdown: "))
countdown(prompt)