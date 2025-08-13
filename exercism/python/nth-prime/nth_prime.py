def prime(n):
    if n == 0:
        raise ValueError("there is no zeroth prime")

    LIMIT = 1_000_000
    primes = [True] * LIMIT
    primes[0] = primes[1] = False  
    for i in range(2, int(LIMIT**0.5)+1):
        if primes[i]:
            for j in range(i*i, LIMIT, i):
                primes[j] = False

    found_primes = [i for i, is_prime in enumerate(primes) if is_prime]
    return found_primes[n-1]

