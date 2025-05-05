class test:
    count=0
    def __init__(self):
        test.count+=1
        print('total no object:',test.count)
    def m1(self):
        test.count+=1
        print('total no object:', test.count)
d=test()