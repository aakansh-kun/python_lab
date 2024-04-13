#define a class named shape and its subclass square. the square class has an init function whic takes a length as argument. both classes has an area function which can print the area of the shape where shape's area is 0 by default.
class shape:
    def __init__(self):
        self.area=0
        
    def calc_area(self):
        return self.area
    
class Square(shape):
    def __init__(self,length):
        self.length= length
        
        
    def calc_area(self):
        self.area= self.length * self.length
        return self.area
    

square = Square(4)
print(square.calc_area())

class Circle(shape):
    def __init__(self,length):
        self.length= length
        
    def calc_area(self):
        self.area= 3.14*self.length * self.length
        return self.area
    
circle=Circle(10)
print(circle.calc_area()) 

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def calc_area(self):
        self.area =self.length * self.width
        return self.area
    
rectangle=rectangle(4,5)
print(rectangle.calc_area())

      

        
