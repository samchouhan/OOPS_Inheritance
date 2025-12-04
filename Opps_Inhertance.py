#Inheritance can be applied within classes too 
#For example if I made a  class and want to make a new class with a new name,that would give error but if i use polymorphism
#The new class made will have everthing that was in the previous class

class Employee:#parent CLASS
   def __init__(self,name,id):
     self.name=name
     self.id=id
    
   def showDetails(self):#Child class which has parent class properties
      print("The name of Employee:",self.id," is ",self.name)  
      
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python" )
    
    
    
e1=Employee("Rohan Das",400)
e1.showDetails()
e2=Programmer("Harry",400)
e2.showDetails()