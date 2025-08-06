def value(colors):
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
    n = 2
    if colors[0] == "black" : 
        del colors[0]
        n=1
    return int(''.join(str(code.index(colors[i])) for i in range(n)))




print(value(["green", "brown", "orange"]))