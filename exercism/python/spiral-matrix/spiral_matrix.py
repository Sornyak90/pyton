def spiral_matrix(size):
    array = [[0 for _ in range(size)] for _ in range(size)]
    i,j, num = 0, 0, 1
    while num < size**2 + 1:
        for j in range(j,size):
            if array[i][j] == 0:
                array[i][j] = num
                num+=1
            else:
                j-=1
                break
        i+=1
            
        for i in range(i,size):
            if array[i][j] == 0:
                array[i][j] = num
                num+=1
            else:
                i-=1
                break
        j-=1

        for j in range(j, -1, -1):
            if array[i][j] == 0:
                array[i][j] = num
                num+=1
            else:
                j+=1
                break
        i-=1
        
        for i in range(i, -1, -1):
            if array[i][j] == 0:
                array[i][j] = num
                num+=1
            else:
                i+=1
                j+=1
                break
            
    return array
