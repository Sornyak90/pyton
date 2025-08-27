class Queen:
    def __init__(self, row=None, column=None):
        self.row = check_err_row(row)
        self.column = check_err_col(column)

    def can_attack(self, another_queen):
        q1 = self
        q2 = another_queen
        result = False

        if q1.row == q2.row and q1.column == q2.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        #I part
        if (q1.row >= q2.row) and (q1.column >= q2.column):
            for i in range(q1.row,-1,-1):
                if  q1.row-i == q2.row and q1.column == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row == q2.row and q1.column-i == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row-i == q2.row and q1.column-i == q2.column:
                    return True

        #II part
        if (q1.row >= q2.row) and (q1.column <= q2.column):
            print((q1.row))
            for i in range(q1.row,-1,-1):
                if  q1.row-i == q2.row and q1.column == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row == q2.row and q1.column+i == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row-i == q2.row and q1.column+i == q2.column:
                    return True
        #III part
        if (q1.row <= q2.row) and (q1.column >= q2.column):
            for i in range(q1.row,-1,-1):
                if  q1.row+i == q2.row and q1.column == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row == q2.row and q1.column-i == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row+i == q2.row and q1.column-i == q2.column:
                    return True


        #IV part
        if (q1.row <= q2.row) and (q1.column <= q2.column):
            for i in range(q1.row,-1,-1):
                if  q1.row+i == q2.row and q1.column == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row == q2.row and q1.column+i == q2.column:
                    return True
            for i in range(q2.column,-1,-1):
                if  q1.row+i == q2.row and q1.column+i == q2.column:
                    return True
        

        return result

def check_err_row(row):
    if row < 0:
        raise ValueError("row not positive")
    if row > 7:
        raise ValueError("row not on board")
    
    return row

def check_err_col(column):
    if column < 0:
        raise ValueError("column not positive")
    if column > 7:
        raise ValueError("column not on board")

    return column