def is_valid(isbn):
    res=False
    sum_n=0
    i=10
    cleaned_text = ''.join(char for char in isbn if char.isalnum()) 
    print(cleaned_text)
    if len(cleaned_text) != 10:
        res=False
    elif any(c.isalpha() for c in cleaned_text[:-1]):
        res=False
    elif cleaned_text[-1] != 'X' and not cleaned_text.isdigit():
        res=False
    else:
        if len(cleaned_text) == 10:
            for num in cleaned_text:
                if num != 'X':
                    sum_n+= int(num) * i
                    i-=1
                else:
                    sum_n+= 10 * i
                    i-=1
    
    if sum_n % 11 == 0 and sum_n != 0:
        res = True
           
    return res

print(is_valid("3598215088"))
