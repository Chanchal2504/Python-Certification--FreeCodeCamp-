class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return (2*(self.width+self.height))
    def get_diagonal(self):
        return (self.width**2 +self.height**2)**0.5
    def get_picture(self):
        shape=""
        if self.width<=50 and self.height<=50:
            for i in range(self.height):
                shape+="*"*self.width+"\n"
        else:
            return "Too big for picture."
        return shape
    def __str__(self):
        obj=f"Rectangle(width={self.width}, height={self.height})"
        return obj
    def get_amount_inside(self,shape):
        amount=self.get_area()//shape.get_area()
        return amount
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)
    def set_width(self,length):
        super().__init__(length,length)
    def set_height(self,length):
        super().__init__(length,length)
    def set_side(self,length):
        self.width=length
        self.height=length
    def __str__(self):
        obj=f"Square(side={self.width})"
        return obj

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))