"""
Accessing the elements from a class and we don't have to use it outside the class.
Access modifiers are rules used to set the visibility of class variables and methods.
They control who can access the data and who cannot.
There are 3 modifiers:
1. Public (no symbol) - Accessible from anywhere.
2. Protected (single underscore _) - Accessible within the class and subclass.
3. Private (double underscore __) - Accessible only within the class.
"""

class demo:
    def __init__(self):
        self.__x=20 #private
        self._y=40  #protected
        self.z=30   #public
d=demo()
print(d.z)  #accessible outside the class
print(d._y)  #can still access, but not recommended
#print(d.__x)  cannot access it , error
print(d._demo__x)  #accessible through mangling(not recommended)

# Setter and Getter methods:
# These two terms help us in controlling how we access and modify the data inside a class.
# - Data should be protected.
# - Data should not be directly modified from outside.
# Setters and getters help us achieve this very easily in Python.

# GETTER:
# A getter is a method that returns the value of a private attribute.
# It is used to access the private data safely.

# SETTER:
# A setter is a method that sets or updates the value of a private attribute.
# It is used to control how data is changed.
class student:
    def __init__(self):
        self.__marks = 0  # Initialize __marks with a default value

    #getter methods
    def get_marks(self):
        return self.__marks
    #setter method
    def set_marks(self,value):
        if value>=0:
            self.__marks=value
        else:
            print("marks can not be negative")
student1=student()
print(student1.get_marks())
student1.set_marks(95)
print(student1.get_marks())