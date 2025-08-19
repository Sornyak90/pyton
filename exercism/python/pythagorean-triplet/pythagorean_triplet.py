def triplets_with_sum(number):
    a = b = 0
    c = number
    result = []
    for a in range(1, number + 1):
        for b in range(a, number + 1):
            c = number - a - b
            if a < b < c and a**2 + b**2 == c**2:
                result.append([a, b, c])
    return result
