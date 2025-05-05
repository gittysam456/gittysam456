class Student:
    def __init__(self, name, age, grade, brand, price):
        self.name = name
        self.age = age
        self.grade = grade
        self.brand = brand
        self.price = price

    def introduce(self):
        print('--student info--')
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

# Creating and introducing students
s1 = Student(name='John', age=20, grade='A', brand='Nike', price=100)
s1.introduce()

s2 = Student(name='Jane', age=22, grade='B', brand='Adidas', price=120)
s2.introduce()
