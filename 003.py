number = 600851475143
# number = 13195

number_for_process = int(number/2)

def prime_check(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime

for i in range(2, number_for_process):
    if prime_check(i):
        if number % i == 0:
            print(i)