# f=open('example.txt','r')

# text=f.read()
# print(text)
# f.close()

#Writing if usinf write the it overwrites the file data ,,,append adds you data at the end 

f=open('example.txt','a')
f.write('Hello,world!')
f.close()
# if we use with we need not to close thefile 
#  with open('example.txt','a')
#  f.write('Hello,world!') 