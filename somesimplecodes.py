"""
create a class where each student has thier own marks and you can calculate thier average
"""
class Student:
    def __init__(self,marks,name):
        self.marks = marks
        self.name=name

    def average(self):
        return sum(self.marks) / len(self.marks)

student1=Student("Amit",[80,90,85])
print(student1.name,"average",student1.average)
