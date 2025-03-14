numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    if number <= 1:
        continue

    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')