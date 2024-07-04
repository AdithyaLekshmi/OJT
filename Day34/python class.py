# Python Class
class Student: 
    """
    This is a class for creating Student objects.
    """
    def __init__(self, name, age, grade): 
        self.name = name 
        self.age = age 
        self.grade = grade

# Create an instance of the Student class
student1 = Student('Neeraj', 12, 'A') 

# Access the attributes of the student1 object
print(student1.name)   # Output: Neeraj
print(student1.age)    # Output: 12
print(student1.grade)  # Output: A

print(Student.__doc__)     
print(Student.__name__)   
print(Student.__module__)  
print(Student.__bases__)   
print(Student.__dict__)    

# Create more instances of the Student class
student2 = Student("A", 1, "A") 
student3 = Student("B", 2, "B")

# Delete the instances
del student2
del student3


# Functions in Classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def displayStudent(self):
        return "Student name is " + self.name + " and age is " + str(self.age)

# Create an instance of the Student class
student1 = Student("BOB", 21, "A")

# Call the displayStudent method and print the result
print(student1.displayStudent())