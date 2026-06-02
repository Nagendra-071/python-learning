import pypdf 
writer=pypdf.PdfWriter()


def merge(pdf_to_merge):
  
    for file in pdf_to_merge:
            writer.append(file)
        
    writer.write('C:\LEARNED\Kaam ke\python/merged.pdf')
    
    
    

n=int(input("Enter the no. of pdf you want to merge: "))
if n<2 :
    print("Minimum 2 pdf required to merge!! ")
else:
    pdf=[]
    for i in range(1,n+1):
        path = input(f"Enter the path for file {i} :").strip('"\'')
        pdf.append(path)
        
    print("\nthis is the order  the file  will be  merged: " )
    for i,file in enumerate(pdf,start=1):
        print(f"index: {i}, {file}")
        
    pdf_dict = {i: file for i, file in enumerate(pdf, start=1)}
    
    ok=int(input(" \n if  Order is correct Enter 1 else 0 for rearrange :"))
    
    if ok==1:
        merge(pdf)
        print("Your pdf is located inside ""C:\LEARNED\Kaam ke\python""")
    
    else:
        rearranged=input("Enter the order  using Index assigned to the files:")
        new_pdf=tuple(int(num) for num in rearranged.split())
        ordered_files = [pdf_dict[index] for index in new_pdf]
        merge(ordered_files) 
        print("\nSuccess! Your rearranged pdf is located inside: C:\\LEARNED\\Kaam ke\\python\\merged.pdf")
    
    
        
        
        
        
    
        
    
        