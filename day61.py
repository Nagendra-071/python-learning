class MyClass:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Value is {self.id} with name  {self.name}") 
 
class Programmer(MyClass):
    def showLanguage(self):
        
         print("Default language is python")
         
e1=MyClass("arun",22)
e2=Programmer('Arjeet',221)
e1.show()
e2.show()
e2.showLanguage()
    