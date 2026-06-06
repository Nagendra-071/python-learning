a=input("NUmber: ")
print("Mutliplication table is")

try:
    for i in range (1,11):
        print(f"{int(a)} X {int(i)} = {int(a)*i}")
except Exception as e:
    print(e)
    
print("Continue rest of the code") 