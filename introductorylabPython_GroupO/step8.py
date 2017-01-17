name = raw_input("Name: ")
try:
    fileOpen = open(name + ".txt", "r")
    newName = raw_input("Name out file: ")
    newFile = open(newName + ".txt", "w")

    for line in fileOpen:
        ascii = ','.join(str(ord(c)) for c in line)
        asciiARRAY = ascii.split(',')
        asciiTABLE = []
        nova = []
        for x in sorted(asciiARRAY):
            asciiTABLE.append(int(x))
        final = sorted(asciiTABLE)

        for x in final:
            if x not in nova:
                nova.append(x)

        print nova
        s = "".join([chr(c) for c in nova])
        print s
        newFile.write(s + '\n')
    fileOpen.close()
except IOError:
    print "File not found"
