import os
files=os.listdir("day46/Tutorial 6")

for i,file in enumerate(files,start=1):
    if file.endswith(".png"):        
        os.rename(f"day46/Tutorial 6/{file}",f"day46/Tutorial 6/{i}.png")
 

