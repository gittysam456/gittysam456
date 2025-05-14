"""


---

A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam. A student is identified by their student ID, age, and marks in the qualifying exam. Data are considered valid if the age is greater than 20 and the marks are between 0 and 100 (both inclusive). A student qualifies for admission if both the age and marks are valid, and the marks are 65 or more.

You are required to write a Python program to represent the students seeking admission in the university. The details of the student class are given below:

**Class Name**: `Student`
**Attributes (Private)**:

* `student_id`
* `marks`
* `age`

**Methods (Public)**:

* `__init__()` – Create and initialize all instance variables to `None`.
* `validate_marks()` – If data is valid (i.e., marks are between 0 and 100), return `True`; else, return `False`.
* `validate_age()` – If age is greater than 20, return `True`; else, return `False`.
* `check_qualification()` – First validate marks and age. If both are valid and marks are 65 or more, return `True`; otherwise, return `False`.
* Setter methods – Include setter methods for all instance variables to set their values.
* Getter methods – Include getter methods for all instance variables to get their values.

---

### Problem Statement:
 a student who is eligible for admission must choose a course and pay the fees for it. If the student has scored more than 85 marks in the qualifying exam, they get a 25% discount on the course fees.

The valid course IDs and corresponding fees are:

| Course ID | Fees    |
| --------- | ------- |
| 1001      | 25575.0 |
| 1002      | 15500.0 |

You are required to extend the program written in the previous assignment to include the above requirement.

The instance variables and methods to be included in the `Student` class for this extension are specified but not detailed in the original text. You will likely need to add attributes for `course_id` and `fees`, methods to validate the course, and a method to calculate discounted fees based on the marks.

---
"""
class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = 0
        self.__age = None
        self.__course_id =None
        self.__fees=0.0

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
        else:
            return False
    def validate_age(self):
        if self.__age > 20:
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
    def set_course_id(self,course_id):
        self.__course_id=course_id
    def get_course_id(self):
        return self.__course_id
    def set_fees(self,fees):
        self.__fees=fees
    def get_fees(self):
        return self.__fees
    def calculate_fees(self):
        if self.__marks > 85:
            return self.__fees * 0.75
        else:
            return self.__fees

    def
