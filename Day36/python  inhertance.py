class father: 
 def father_name(self):
    print("My father name is Suresh")

class son(father): 
 pass

obj_father= father() 
obj_son=son() 
obj_son.father_name() 
# Multilevel inheritance


class g_father:
    def g_father_name(self):
        print("my father name is Suresh")

class father(g_father):
 def father_name(self):
    print("my Mother name is Sheeja")

class son(father):
 def son_name(self):
    print("my name is Adithya")


 obj_g_father= father() 
 obj_father= father()
obj_son=son()

obj_son.g_father_name() 
obj_son.father_name()
# Multiple Inheritance
class father: # parent class
  def father_name(self):
    print("my father name is Suresh Kumar")

class mother: # parent class
  def mother_name(self):
    print("my father name is Suresh")

class son(mother,father): # child class
  pass

obj_father= father() 
obj_mother=mother() 
obj_son=son() 

obj_son.father_name() 
obj_son.mother_name() 

# obj_mother.father_name() # This statement did not work because mother and father are parents. Output 