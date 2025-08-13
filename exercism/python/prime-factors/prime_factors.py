def factors(value):
    res =[]
    if value > 1:
        i = 2
        while value != 1:
            if value % i == 0:
                value//=i
                res.append(i)
                i = 2
            else:
                i+=1
    return res

print(factors(4))

