class Pen:
    def _init_(self):
      self.brand='link'
      self.color='Red'
      self.price=20
    def show_pen_detail(self):
       print(self.color)
       print(self.brand)
p1=Pen('link','Red',20)
p1.show_pen_detail()

p2=Pen('parker','Blue',30)
p2.show_pen_detail()
