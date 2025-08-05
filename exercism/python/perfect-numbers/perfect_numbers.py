def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    res = ''
    num = 0

    if number <= 0:\
        raise ValueError("Classification is only possible for positive integers.")
    
    for i in range(1,number):
        if number % i == 0:
            num+=i

    if num == number:
        res = 'perfect'
    elif num > number:
        res = 'abundant' 
    else:
        res = 'deficient'
    
    return res

print(classify(8))
