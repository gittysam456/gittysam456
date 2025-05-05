class Demo:
    A=65
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def m1(self,z):
        self.z=z
        
d1=Demo(10,20)
#d2=Demo(110,120)
d1.m1(20)
d1.z=456
print(d1.__dict__)
d1.t=478
print(d1.__dict__)
