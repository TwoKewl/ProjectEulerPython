def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False

    for i in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

def is_pandigital(number):
    number_str = str(number)
    length = len(number_str)
    expected_digits = set(str(i) for i in range(1, length + 1))
    
    return set(number_str) == expected_digits

a = sieve_of_eratosthenes(10000000)

for i in a:
    if is_pandigital(i):
        print(i)