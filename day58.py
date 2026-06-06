# class Person:
#     name="Harry"
#     occ="Developer"
    
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a=Person()
# print(a.name)

# a.info()

class Person:  
    def __init__(self,n,o):
        print("Hey i am a person")
        self.name=n
        self.occ=o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("Harry","Developer")
a.info()
 