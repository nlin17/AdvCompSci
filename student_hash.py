class Student:
    def __init__(self, id, fn, ln, gl, gpa):
        self.id = id
        self.first_name = fn
        self.last_name = ln
        self.grade_level = gl
        self.gpa = gpa
    
    def __hash__(self):
        return hash((self.id, self.first_name, self.last_name, self.grade_level, self.gpa))
        # get the hash of the student object
    
    def print_hash(self):
        return hash(self)
    
ben = Student(1, 'Ben', 'Smith', 12, 3.5)
print(ben.print_hash())
       