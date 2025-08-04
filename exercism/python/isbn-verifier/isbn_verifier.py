def is_valid(isbn):
    cleaned = ''.join(c for c in isbn if c.isalnum())
    if len(cleaned) != 10:
        return False
    if any(c.isalpha() for c in cleaned[:-1]):
        return False
    if cleaned[-1] not in '0123456789X':
        return False
    
    total = 0
    for i, char in enumerate(cleaned):
        value = 10 if char == 'X' else int(char)
        total += value * (10 - i)
    
    return total % 11 == 0 and total != 0