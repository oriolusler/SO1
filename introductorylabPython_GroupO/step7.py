name = raw_input("Name: ")
fileOpen = open(name + ".txt", "r")
newName = raw_input("Name out file: ")
newFile = open(newName + ".txt", "w")
for line in fileOpen:
    ascii = ','.join(str(ord(c)) for c in line)
    asciiARRAY = ascii.split(',')
    asciiTABLE = []

    for x in sorted(asciiARRAY):
        asciiTABLE.append(int(x))
    final = sorted(asciiTABLE)
    print final
    s = "".join([chr(c) for c in final])
    print s
    newFile.write(s+'\n')
fileOpen.close()