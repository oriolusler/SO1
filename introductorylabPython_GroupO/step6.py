name = raw_input("Name: ")
try:
    newName = raw_input("Name out file: ")
    newFile = open(newName + ".txt", "w")
    counter = 0
    with open(name + '.txt') as f:
        total = sum(1 for _ in f)
    for line in reversed(open(name + ".txt").readlines()):
        lineC = str(total - counter) + " " + line.rstrip() + "\n"
        counter += 1
        print lineC
        newFile.write(lineC)
except IOError:
    print "File not found"
