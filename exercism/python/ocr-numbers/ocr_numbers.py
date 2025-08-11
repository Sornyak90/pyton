def convert(input_grid):
    digit = {
        "010202212000" : "0",
        "000002002000" : "1",
        "010012210000" : "2",
        "010012012000" : "3", 
        "000212002000" : "4",
        "010210012000" : "5",
        "010210212000" : "6",
        "010002002000" : "7",
        "010212212000" : "8",
        "010212012000" : "9"
    }
    
    res_digit = ""
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    for i in input_grid:
        if len(i) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    
    for t in range(0, len(input_grid), 4):
        for i in range(0,len(input_grid[t]), 3):
            result = ""
            for j in range(t,t+4):
                for g in range(i,i+3):
                    if input_grid[j][g] == " ":
                        result += "0"
                    if input_grid[j][g] == "_":
                        result += "1"
                    if input_grid[j][g] == "|":
                        result += "2" 
            if result in digit:
                res_digit+=digit[result]
            else:
                res_digit+="?" 

        if t < len(input_grid) - 4:
                    res_digit+= ','    

    return res_digit   