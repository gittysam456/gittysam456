"""
A university wants to automate their admission process. Students are admitted based on the marks scored in a qualifying exam. A student is identified by their student ID, age, and marks in the qualifying exam. The data is considered valid if the student's age is greater than 20 and the marks are between 0 and 100 (both inclusive). A student qualifies for admission if the data is valid and the marks are 65 or more.

You are required to write a Python program to represent students seeking admission to the university. The details of the student are encapsulated in a class as described below:

**Class Name**: `Student`
**Attributes (Private)**:

* `student_id`
* `marks`
* `age`

**Methods (Public)**:

* `__init__()` – Initializes all instance variables to `None`.
* `validate_marks()` – Returns `True` if marks are between 0 and 100, otherwise returns `False`.
* `validate_age()` – Returns `True` if age is greater than 20, otherwise returns `False`.
* `check_qualification()` – Validates age and marks. If both are valid and marks are 65 or more, returns `True`. Otherwise, returns `False`.
* Setter methods – Set the values of `student_id`, `marks`, and `age`.
* Getter methods – Get the values of `student_id`, `marks`, and `age`.
"""
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = 0
        self.__age = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age
    def validate_marks(self):
        if 0 <= self.__marks <= 100:
            return True
        else
            return False
    def validate_age(self):
        if self.__age > 20
            return True
        else:
           return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65:
                return True
            else:
                return False
        else:
            return False
