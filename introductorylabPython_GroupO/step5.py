name = raw_input("Name: ")
fileOpen = open(name + ".txt", "r")
newName = raw_input("Name out file: ")
newFile = open(newName + ".txt", "w")
for line in fileOpen:
    print(line)
    newFile.write(str(len(line) - 1) + " " + line)
fileOpen.close()