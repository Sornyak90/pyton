def is_armstrong_number(number):
    s = str(number)
    n = len(s)
    res=0
    for i in range(n):
        res+=int(s[i]) ** n  
    return res == number
