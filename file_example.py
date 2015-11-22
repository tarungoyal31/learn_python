from sys import argv 

script, fileName = argv

txt = open(fileName, "r+")

print "%s content\n" % fileName
print txt.readline(),
print txt.readline(),
print "Enter content to be added to the file"
newLine = raw_input("line 1: ")
txt.write(newLine+"\n")
txt.close()
txt = open(fileName)
print "new complete content of the file\n", txt.read()
txt.close()
