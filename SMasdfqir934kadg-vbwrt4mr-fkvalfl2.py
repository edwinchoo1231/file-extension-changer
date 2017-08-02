import os

print("Path at terminal when executing this file")
print(os.getcwd()+ "\n")
#C:\IBM\Control Panel  
#print("This file path, relative to os.getcwd()")
#print(__file__ + "\n")

#print("This file full path (following symlinks)")
#full_path = os.path.realpath(__file__)
#print(full_path + "\n")

#print("This file directory and name")
#path, filename = os.path.split(full_path)
#print(path + ' --> ' + filename + "\n")

#print("This file directory only")
#print(os.path.dirname(full_path))

file=os.listdir(os.getcwd())
#print(file)
length = len(file)

print(file)
print(length)
print(file[0])
thisFile = file[0]
# = os.path.splitext(thisFile)

#print(base,ext)
for i in file:
    base, ext = os.path.splitext(i)
    if (ext=='.txt'):
        os.rename(i, base + ".jpeg")

    elif (ext=='.jpeg'):
        os.rename(i, base + ".txt")
    print(i)

#os.rename(thisFile, base + ".txt")
filen = os.listdir(os.getcwd())
print(filen)
