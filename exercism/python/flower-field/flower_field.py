def annotate(garden):
    # Function body starts here
    if len(set(len(s) for s in garden)) > 2:
        raise ValueError("The board is invalid with current input.")

    if len(set(s for row in garden for s in row)) > 2:
        raise ValueError("The board is invalid with current input.")

    if len(garden) != 0 and len(garden[0]) != 0:
        max_i = len(garden)
        max_j = len(garden[0])

        garden = [list(i) for i in garden]

        for i in range(max_i):
            for j in range(max_j):
                if garden[i][j] == "*":
                    for g in range(-1, 2):
                        for h in range(-1, 2):
                            x = i + g
                            y = j + h
                            if (0 <= x < max_i) and (0 <= y < max_j):
                                if garden[x][y] != "*":
                                    if garden[x][y] == " ":
                                        garden[x][y] = "1"
                                    else:
                                        num = int(garden[x][y])
                                        num += 1
                                        garden[x][y] = str(num)
                            else:
                                continue

        result = ["".join(row) for row in garden]
    else:
        result = garden

    return result
