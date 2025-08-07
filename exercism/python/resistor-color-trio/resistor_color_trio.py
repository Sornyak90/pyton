def label(colors):
    resist = 0
    code = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
        ]
    
    if len(colors) > 3:
        colors.pop()

    n = 2
    while len(colors) != 0 and colors[0] == "black": 
        del colors[0]
        n=1
    
    if len(colors) != 0:
        resist = ''.join(str(code.index(colors[i])) for i in range(n))
        resist = resist + '0' * code.index(colors[-1])
        count_zero = resist.count('0')
        zero = int(count_zero / 3)
        
        if zero == 0:
            resist = resist + ' ohms'
        elif  zero == 1:
            resist = resist[:-3] + ' kiloohms'
        elif  zero == 2:
            resist = resist[:-6] + ' megaohms'
        elif  zero == 3:
            resist = resist[:-9] + ' gigaohms'
    else:
        resist = '0 ohms'

    return resist


print(label(["black", "black", "black"]))