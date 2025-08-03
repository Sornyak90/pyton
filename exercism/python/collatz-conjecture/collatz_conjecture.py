def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    step = 0
    current = number
    
    while current != 1:
        if step > 1000:  # Защита от возможного бесконечного цикла
            raise RuntimeError("Maximum step count exceeded")
        
        if current % 2 == 0:
            current = current // 2  # Целочисленное деление
        else:
            current = current * 3 + 1
        step += 1
    
    return step
        
    

