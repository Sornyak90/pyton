class Garden:
    DEFAULT_STUDENTS = [
            "Alice", "Bob", "Charlie", "David",
            "Eve", "Fred", "Ginny", "Harriet",
            "Ileana", "Joseph", "Kincaid", "Larry"
        ]
    

    def __init__(self, diagram, students = DEFAULT_STUDENTS):
        self.diagram = diagram
        self.students = students
        

    def plants(self, student):
        flowers = {
                "G": "Grass",
                "C": "Clover",
                "R": "Radishes",
                "V": "Violets"
        }

        diagrams = self.diagram.replace("\n","")
        pairs = [diagrams[i:i+2] for i in range(0, len(diagrams), 2)]
        result = {} 
        list_flowers = []
        students = sorted(self.students)

        idx_1=0
        idx_2=(len(pairs)//2)
        for stud_n in students:
            if idx_1 < (len(pairs)/2):
                result[stud_n] = [pairs[idx_1], pairs[idx_2]]
                idx_1 += 1
                idx_2 += 1
            else:
                result[stud_n] = []
        
        ch = result[student]
        lst_str = ''.join(ch)

        for n in lst_str:
            list_flowers.append(flowers[n])

        return list_flowers
