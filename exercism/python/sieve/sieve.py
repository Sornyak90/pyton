def primes(limit):
    sieve = {k : True for k in range(2,limit+1)} 
    result = []

    for key in sieve.keys():
        if sieve[key]:
            for i in range(key+1,len(sieve)+2):
                if i % key == 0:
                    sieve[i] = False
    
    for key in sieve.keys():
        if sieve[key]: 
            result.append(key)

    return result


# primes(13)