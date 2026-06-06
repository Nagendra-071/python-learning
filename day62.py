class MyClass:
    def __init__(self):
        self.name="Harry"   #public
        self.__class="Lkg"  #private
        
        
a=MyClass()
print(a.name)
print(a._MyClass__class)