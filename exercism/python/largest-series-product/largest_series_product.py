from math import prod
def largest_product(series, size):

    if len(series) < size or not series:
        raise ValueError("span must not exceed string length")
    
    if any(not char.isdigit() for char in series):
        raise ValueError("digits input must only contain digits")
    
    if size < 0:
        raise ValueError("span must not be negative")

    max_mul = 0
    for i in range(len(series)-size+1):
        series = list(map(int, series))
        mul_dig = prod(series[i:i+size])
        if mul_dig > max_mul:
            max_mul = mul_dig
    return max_mul