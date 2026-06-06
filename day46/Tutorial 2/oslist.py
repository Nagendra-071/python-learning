import os

folders= os.listdir("day46")
print(folders)

for folder in folders:
    print(os.listdir(f"day46/{folder}"))