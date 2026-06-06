import shutil
import os

#copy a file 
shutil.copy("day46/Tutorial 2/oslist.py","oslist2.py")

#copy a folder
shutil.copytree("day46", "nelist")


#move a file to other location
shutil.move("day46/tutorial 2/renam.py","newfile")

#delete a folder
shutil.rmtree("day46/tutorial 2")

#file remove
os.remove("day46/tutorial 2/renam.py") 