class School:
    def __init__(self):
        self.list_name = {}
        self.lits_added = []
    
    def add_student(self, name, grade):
        if name not in self.list_name:
            self.list_name[name] = grade
            self.lits_added.append(True)
        else:
            self.lits_added.append(False)

    def roster(self):
        sorted_grade = sorted(self.list_name.items(), key=lambda x: (x[1], x[0]))
        name = [item[0] for item in sorted_grade]
        return name

    def grade(self, grade_number):
        result = []
        for key, value in self.list_name.items():
            if value == grade_number:
                result.append(key)
        return sorted(result)

    def added(self):
        return self.lits_added



        
