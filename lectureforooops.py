"""class demo:

    def __init__(self):
        print('construct......')
        self.m1()
        self.m2()
        self.m3()
        ####
        #demo.m1() invalid method
        demo.m2()
        demo.m3()

    def m1(self):
        print("instance method")
    @classmethod
    def m2(cls):
        print('class method')
    @staticmethod
    def m3():
        print("static method")
d=demo()
print("*"*25)
######################
class demo:

    def __init__(cls):
        print('construct......')
        demo.m2()
        demo.m3()

    def m1(self):
        print("instance method")
    @classmethod
    def m2(cls):
        print('class method')
    @staticmethod
    def m3():
        print("static method")
d=demo()
print("*"*25)

"""
class demo:

    def __init__(self):
        print('construct......')
       

    def m1(self):
        print("instance method")
        demo.m2()
        demo.m3()
    @classmethod
    def m2(cls):
        print('class method')
        #demo.m3()
        #cls.m3()
    @staticmethod
    def m3():
        print("static method")
        #demo.m1()
        demo.m2()
        cls.m2()
        #cls.m1()
        #self.m1()
        self.m2()
d=demo()
