def sum_of_multiples(limit, multiples):
    sum_of_multi = []
    for n in multiples:
        for i in range(1, limit):
            if  n != 0 and i % n == 0:
                sum_of_multi.append(i)

    return sum(set(sum_of_multi))  
