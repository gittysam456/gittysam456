class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def introduce(self):
        print('--student info')
        print(self.name)
        print(self.brand)
        print(self.price)
    
    s1=Student('John', 20, 'A')
    s1.introduce()
    s2=Student('Jane', 22, 'B')
    s2.introduce()
