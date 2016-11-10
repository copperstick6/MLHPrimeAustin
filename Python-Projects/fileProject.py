#open the file if it exists, write if it doesn't
#w+ represents create
f = open("newFile.txt", "w+")
for x in range (0,10):
    f.write("this is line %d\r\n" %(x+1))

f.close
