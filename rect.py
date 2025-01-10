class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
       return self.length*self.width
    def calculate_perimeter(self):
       return 2*(self.length+self.width)
length=float(input("enter length of rectangle:"))
width=float(input("enter the width of rectangle:"))
rectangle=Rectangle(length,width)
print("area of the rectangle:",rectangle.calculate_area())
print("perimeter of the rectangle:",rectangle.calculate_perimeter())