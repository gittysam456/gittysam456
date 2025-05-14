"""
A university
wants
to
automate
their
admission
process.Students
are
admitted
based
on
marks
scored in a
qualifying
exam.
A
student is identified
by
student
id, age and marks in qualifying
exam.Data
are
valid,
if:

Age is greater
than
20
Marks is between
0 and 100(both
inclusive)
A
student
qualifies
for admission, if

Age and marks
are
valid and
Marks is 65 or more
Write
a
python
program
to
represent
the
students
seeking
admission in the
university.

The
details
of
student


class are given below.


Class
name: Student

Attributes
(private)

student_id
marks
age

Methods
(public)

__init__()

Create and initialize
all
instance
variables
to
None

validate_marks()

If
data is valid,
return true.Else,
return false

validate_age()

check_qualification()

Validate
marks and age.

If
valid, check if marks is 65 or more.
If
so
return true
Else
return false
Else
return false

setter
methods

Include
setter
methods
for all instance variables to set its values

getter
methods

Include
getter
methods
for all instance variables to get its values
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