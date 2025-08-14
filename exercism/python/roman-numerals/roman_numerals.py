def roman(number):
    digit_arab = ""
    while number >= 900:
        if 1000 > number >= 900:
            digit_arab += 'CM' 
            number-=900 
        else:
            digit_arab += 'M' 
            number-=1000

    while number >= 400:
        if 500 > number >= 400:
            digit_arab += 'CD' 
            number-=400 
        else:
            digit_arab += 'D' 
            number-=500
    
    while number >= 90:
        if 100 > number >= 90:
            digit_arab += 'XC' 
            number-=90 
        else:
            digit_arab += 'C' 
            number-=100
    
    while number >= 40:
        if 50 > number >= 40:
            digit_arab += 'XL' 
            number-=40 
        else:
            digit_arab += 'L' 
            number-=50 
    
    while number >= 9:
        if number == 9:
            digit_arab += 'IX' 
            number-=9 
        else:
            digit_arab += 'X' 
            number-=10 
        

    while number >= 5:
        number-=5
        digit_arab += 'V'

    while number >= 1:
        if number > 3:
            digit_arab += 'IV' 
            number-=4 
        else:
            digit_arab += 'I' 
            number-=1 

    reversed(digit_arab)
    return digit_arab
    
    

