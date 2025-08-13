def slices(series, length):
    res = []

    if length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif series == "":
        raise ValueError("series cannot be empty")
    elif len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    for i in range(0,len(series) - length+1):
        res.append(series[i:i+length])
    return res



print(slices("1", 1))
