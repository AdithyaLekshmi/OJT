#1. Write a Python program to create a class called Rectangle. 
#The class should have attributes length and width, and 
#methods calculate_area() to calculate the area of the rectangle and 
#calculate_perimeter() to calculate the perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

length = 5
width = 3

rectangle = Rectangle(length, width)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print("Rectangle Area:", area)
print("Rectangle Perimeter:", perimeter)
