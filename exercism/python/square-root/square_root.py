DELTA = 0.0001

def square_root(number):
    x0 =  number/2
    x2 = 1
    while x2 > DELTA:
        x1 = round((x0 + (number/x0))/2,3)
        x2= round(abs(x1 -x0),3)
        x0=x1
        
    return int(x1) 
