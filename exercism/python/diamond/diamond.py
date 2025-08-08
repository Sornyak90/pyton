def rows(letter):
    size = 2 * (ord(letter) - 65) + 1
    center = size // 2
    result = []
    
    for i in range(center + 1):
        row = [' '] * size
        row[center - i] = row[center + i] = chr(65 + i)
        result.append(''.join(row))
    
    return result + result[-2::-1]