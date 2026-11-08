#Q8. Prime check. Write is_prime(n) that returns True or False. Then print all prime numbers from 1 to 50 using it.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


for num in range(1, 51):
    if is_prime(num):
        print(num, end=" ")
