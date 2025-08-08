def annotate(garden):
    if not garden:
        return garden
    
    # Validate board dimensions
    if len({len(row) for row in garden}) > 1:
        raise ValueError("The board is invalid with current input.")
    
    # Validate board characters
    if {char for row in garden for char in row} - {' ', '*'}:
        raise ValueError("The board is invalid with current input.")

    garden = [list(row) for row in garden]
    rows, cols = len(garden), len(garden[0])

    for i in range(rows):
        for j in range(cols):
            if garden[i][j] == '*':
                # Check all 8 surrounding cells
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == dj == 0:
                            continue
                        x, y = i + di, j + dj
                        if 0 <= x < rows and 0 <= y < cols and garden[x][y] != '*':
                            garden[x][y] = '1' if garden[x][y] == ' ' else str(int(garden[x][y]) + 1)

    return [''.join(row) for row in garden]