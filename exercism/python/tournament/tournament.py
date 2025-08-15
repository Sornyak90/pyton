def tally(rows):
    
    table = [
            "Team                           | MP |  W |  D |  L |  P"
    ]
    name = []
    player_result = [0]*5
    table_result = {}

    if rows == []:
        return table

    for i in range(len(rows)):
        line = rows[i].split(";")
        line.pop()
        name+=line
        names = set(name)

    for name in names:
        table_result[name] = player_result.copy()
    
    for i in range(len(rows)):
        line = rows[i].split(";")
        if line[2] == "win":
            table_result[line[0]][0]+=1
            table_result[line[0]][1]+=1
            table_result[line[0]][4]+=3
            table_result[line[1]][0]+=1
            table_result[line[1]][3]+=1
        elif line[2] == "loss":
            table_result[line[1]][0]+=1
            table_result[line[1]][1]+=1
            table_result[line[1]][4]+=3
            table_result[line[0]][0]+=1
            table_result[line[0]][3]+=1
        else:
            table_result[line[0]][0]+=1
            table_result[line[1]][0]+=1
            table_result[line[0]][2]+=1
            table_result[line[1]][2]+=1
            table_result[line[0]][4]+=1
            table_result[line[1]][4]+=1
    

    #спиздил код 
    sorted_table = sorted(table_result.items(), key=lambda x: (-x[1][4], x[0]))
    ######


    for item in sorted_table:
        item_list = list(item)
        table.append(
            item_list[0] + " " * (30 - len(item_list[0])) +
            f" | {' ' if int(item[1][0]) < 10 else ''}{item[1][0]} | " +
            f"{' ' if int(item[1][1]) < 10 else ''}{item[1][1]} | " +
            f"{' ' if int(item[1][2]) < 10 else ''}{item[1][2]} | " +
            f"{' ' if int(item[1][3]) < 10 else ''}{item[1][3]} | " +
            f"{' ' if int(item[1][4]) < 10 else ''}{item[1][4]}"
)
                                                                                                                                   
    return table

table = []
            
print(tally(table))