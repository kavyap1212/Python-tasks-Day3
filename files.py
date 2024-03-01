# 1. Creating text file with function & writing content into it 

import datetime

def create_txt(now):
    # Create a filename with the current datetime timestamp
    filename = now.strftime("%Y-%m-%d_%H-%M-%S.txt")
    # Open the file for writing
    with open(filename, "w") as f:
    # Write some content to the file
        f.write("This is a new file created with Python!: "+"\n" +"Time Stamp: "+ content)
    # Close the file
    f.close()
# Get the current datetime
now = datetime.datetime.now()
content = now.strftime("%Y-%m-%d_%H-%M-%S")
create_txt(now)

# 2. Read from a text file

def read_txt(fname):
    f = open(fname,"r")
    return f.read()
    
print("Enter name of the file to open & read: ")
fname = input()
fname = fname+".txt"
File_content = read_txt(fname)
print(File_content)
