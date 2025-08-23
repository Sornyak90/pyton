class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix = []
        count_row = self.matrix_string.count("\n") + 1
        matrix_list = list(map(int, self.matrix_string.split()))
        count_colm = len(matrix_list)//count_row
        inx=0
        for i in range(count_row):
            matrix.append([])
            for j in range(count_colm):
                matrix[i].append(matrix_list[inx])
                inx+=1

        return matrix[index-1]
      
                
    def column(self, index):
        matrix = []
        result = []
        count_row = self.matrix_string.count("\n") + 1
        matrix_list = list(map(int, self.matrix_string.split()))
        count_colm = len(matrix_list)//count_row
        inx=0
        for i in range(count_row):
            matrix.append([])
            for j in range(count_colm):
                matrix[i].append(matrix_list[inx])
                inx+=1

        for i in range(count_row):
            result.append(matrix[i][index-1])
            
        return result
        


