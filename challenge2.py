#Written by Shiven Desai
class Teacher:
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print('Professor Name is ' + self.name)
        print('Professor assigned class is ' + self.classRoom)
        print('Professor is teaching ' + self.course)

# create Teacher1 object
Teacher1 = Teacher('Prof. Sim', 'A206', 'Python Programming')
Teacher1.GetProfessor()

# create Teacher2 object
Teacher2 = Teacher('Prof. Lee', 'B102', 'Web Development')
Teacher2.GetProfessor()
