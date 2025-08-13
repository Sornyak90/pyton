def square_of_sum(number):
    res = 0
    for i in range(1, number+1):
        res+= i
    return res**2


def sum_of_squares(number):
    res = 0
    for i in range(1, number+1):
        res+= i**2
    return res


def difference_of_squares(number):
    a = square_of_sum(number)
    b = sum_of_squares(number)
    return a - b
