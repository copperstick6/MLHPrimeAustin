#open the file if it exists, write if it doesn't
#w+ represents create
f = open("newFile.txt", "w+")
for x in range (0,10):
    f.write("this is line %d\r\n" %(x+1))

f.close

#open the file to append to the end of the file using a+
f = open("newFile.txt", "a+")
f.write("APPENDED TO THE END!")
f.close

#reading the contents of the text file, printing to output
f = open("newFile.txt","r")
if f.mode == 'r':
    contents = f.read()

print contents

#reading the contents of the file into a list
fl = f.readlines()
for x in fl:
    print x
