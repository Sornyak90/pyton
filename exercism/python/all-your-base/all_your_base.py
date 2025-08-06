def rebase(input_base, digits, output_base):
    result = []
    degree = 0
    in_decimal = 0
    from_decimal = 0
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    for d in digits:
        if d < 0 or  d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not (input_base == 10 and output_base == 2): 
        for i in digits[::-1]:
            in_decimal+= i * input_base**degree
            degree+=1
        from_decimal = in_decimal
    else:
        from_decimal = int(''.join(map(str, digits)))
    
    while from_decimal >= output_base:
        remains = from_decimal % output_base
        from_decimal  = int(from_decimal / output_base)
        result.insert(0,remains)
    else:
        result.insert(0,from_decimal)
    
    return result