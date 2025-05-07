"""
create a class with provate attribute salary
make a getter to view the salary
sette view to change the change the salary , but do allow below the 10000
if trying to set range loweer than 10000, give a warning>
"""
class employee:
def __init__(self):
        #getter methods
    def get_marks(self):
        return self.__salary
    #setter method
    def set_marks(self,value):
        if value>=10000:
            self.__salary=value
        else:
            print("it cannot be lower than 10000")
