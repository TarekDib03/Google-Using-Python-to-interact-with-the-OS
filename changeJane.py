import sys
import subprocess

path = 'C:/Users/Tarek/Documents/Google Using Python to interact with the OS'

with open(sys.argv[1]) as f:
    lines = f.readlines() 
    
    for line in lines:
        old_name = line.strip()
        new_name = old_name.replace("jane","jdoe")
        subprocess.run(["mv", path+old_name, path+new_name])
f.close()

