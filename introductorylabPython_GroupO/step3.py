name = raw_input("Name: ")
fileOpen = open(name + ".txt", "r")
for line in fileOpen:
    print(line)
fileOpen.close()