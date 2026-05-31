import os
pf=os.listdir("day46/Tutorial 6")
files=[ i for i in pf if i.lower().endswith('.png')]
#same hai chahe upar wala likho chhae neeche wala
# files = []
# for file in pf:
#     if file.lower().endswith('.png'):
#         files.append(file)

for i,file in enumerate(files,start=1):
    old_path=os.path.join("day46/Tutorial 6",file)
    
    new_path=os.path.join("day46/Tutorial 6",f"{i}.png")
    os.rename(old_path, new_path)
    

