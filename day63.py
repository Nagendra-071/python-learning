class Library:
    def __init__(self):
        self.books=[]
        self.count=0
        
    def add(self,title):
        self.books.append(title)
        self.count +=1
        
row1=Library()
row1.add("Story of tintin")        
row1.add("1984")

print(f"Row 1 consit of {row1.books} these books") 
print("Total No . of books in row 1 : ",row1.count)

row2=Library()
row2.add("Story  of Bhagat Singh")        
row2.add("LOC")

print(f"Row 2 consit of {row2.books} these books") 
print("Total No . of books in row 2 : ",row2.count)