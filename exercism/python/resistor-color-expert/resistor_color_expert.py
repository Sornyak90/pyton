def resistor_label(colors):
    resist = 0
    code = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    procent = {"grey": "0.05", "violet" : "0.1", "blue" : "0.25", "green" : "0.5", "brown" : "1", "red" : "2", "gold" : "5", "silver" : "10"}


    n = len(colors[:-2])
    while len(colors) != 0 and colors[0] == "black": 
        del colors[0]
        n=1
    
    if len(colors) != 0:
        tmp = colors[-1]
        resist = ''.join(str(code.index(colors[i])) for i in range(n))
        resist = resist + '0' * code.index(colors[-2])
        count_zero = resist.count('0')
        
        if len(resist) < 4:
            resist = resist + ' ohms'
        elif  count_zero  < 4: 
            resist = (str(int(resist)/10**3) if count_zero != 3 else resist[:-3]) + ' kiloohms'
        elif  count_zero < 7:
            resist = (str(int(resist)/10**6) if count_zero != 6 else resist[:-6]) + ' megaohms'
        elif  count_zero < 10:
             resist = (str(int(resist)/10**7) if count_zero != 9 else resist[:-9]) + ' gigaohms'

        resist = f"{resist} ±{procent[tmp]}%"
    else:
        resist = '0 ohms'

    return resist

print(resistor_label(["blue", "grey", "white", "brown", "brown"]))
