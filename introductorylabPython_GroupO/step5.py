name = raw_input("Name: ")
try:
    fileOpen = open(name + ".txt", "r")
    newName = raw_input("Name out file: ")
    newFile = open(newName + ".txt", "w")
    for line in fileOpen:
        finalString=str(len(line) - 1) + " " + line
        print(finalString)
        newFile.write(finalString)
    fileOpen.close()
    newFile.close()
except IOError:
    print"File not found"
