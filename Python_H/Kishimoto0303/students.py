class Student:
    
    def __init__(self, id, name, score = 0):
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def setScore(self,score):
        self.score = score

    def getScore(self):
        return self.score
    
class CalcScore:
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)   

    def ave(self):
         v = 0
         for i in self.students:
             v += i.getScore()
            ave_v = v / len(self.students)
        return ave_v

p1 = Student(10, "佐藤")
p1.setScore(80)
p2 = Student(11, "鈴木", score=79)
p3 = Student(12, "佐々木", score=84)
p4 = Student(13, "井上", score=77)

calc = CalcScore()
calc = addStudent(p1)
calc = addStudent(p2)
calc = addStudent(p3)
calc = addStudent(p4)

print("平均点=", calc.ave())