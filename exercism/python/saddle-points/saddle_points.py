def saddle_points(matrix):
    
    if matrix == []:
        return []
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise ValueError("irregular matrix")
    
    
    len_row = len(matrix)
    len_col = len(matrix[0])
    res = []
   
    for i in range(len_row):
            for j in range(len_col):
                g_line = matrix[i][:len_col]
                v_line = [row[j] for row in matrix]
                if max(g_line) == min(v_line):
                    res+=[{"row": i+1, "column": j+1}]
                    
    return res
