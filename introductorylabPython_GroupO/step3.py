name = raw_input("Name of text file: ")
try:
    fileOpen = open(name + ".txt", "r")
    for line in fileOpen:
        print(line)
    fileOpen.close()
except IOError:
    print ("File not found")
