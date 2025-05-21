#Inheritance
"""
inheritance means one class use the property and method of the another class,just likke child inherit th from parents, a new class (child)can inherit
features fro an existing class(parent)

why use the inheritance?
reusability: write code omce and use it at ,multiple place
simplicity:organize code better
extensibility:easily and new feature.
------------------------------------------------------------------------------------
#Types of the inheritance
1. single inheritance ==> one child inherit from one parent
2. multiple inheritance ==> one child inherit from more than one parent
3. Multilevel inheritance ==> chain of inheritance (child-> parent-> grandparent)
4. Hierarchical inheritance ==> multiple children inherit from one parent
5. Hybrid Inheritance ==> combination of the above any two
"""

# example code single level inheritance
class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def description(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")
class Student(Human):
    def schoolname(self,schoolname):
        print(f"School: {self.schoolname}")
"""
 Hierarchical inheritance
 -->single parent multiple child
 it is the concept where multiple child classes inherit from the same parent class,and all the 
 are at the same level.
 parent---- child1
            ----child2 
child1 and child2 are the child classes of parent class and both inherit from the same parent class.
 """
class Employee(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.companyname = None

    def employeeID(self,employeeID):
        print(f"Employee ID: {self.employeeID}")
    def companyName(self,company_name):
        print(f"Company: {self.companyname}")

#creating object of the class
b=Student('amit',15,'male')
b.description()
b.schoolname('ABC School')

A=Employee('sadaf',22,'female')
A.description()
A.employeeID(12345)
"""
#Multiple inheritance
Multiple inheritance is a type of inheritance in which one child class inherits properties and methods from two.
or more parent classes.
# example code multiple inheritance"""
class Father:
    def skill(self):
        print(f"Father's skill: Driving")
class Mother:
    def skill(self):
        print(f"Mother's skill: Cooking")
class Child(Father,Mother):
    def ownskill(self):
        print(f"Child's skill: Painting")

c=Child()
c.skill()
c.ownskill()