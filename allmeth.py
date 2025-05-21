"""
write a program in python whose class name is parent class in which one static variable ,instance variable
and static method,instance method ann class method and access in child  through inheritance process.
"""
class parent:
    # static variable
    static_variable = 10
    # instance variable
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    # static method
    @staticmethod
    def static_method():
        print("This is a static method of the parent class.")
    # instance method
    def instance_method(self):
        print("This is an instance method of the parent class.")
    # class method
    @classmethod
    def class_method(cls):
        print("This is a class method of the parent class.")
# child class
class child(parent):
    def __init__(self, instance_variable, child_variable):
        # calling parent constructor
        super().__init__(instance_variable)
        self.child_variable = child_variable
    # instance method of child class
    def child_method(self):
        print("This is an instance method of the child class.")
    # accessing parent class static variable
    def access_static_variable(self):
        print(f"static variable: {parent.static_variable}")
    # accessing parent class instance variable
    def access_instance_variable(self):
        print(f"instance variable : {self.instance_variable}")