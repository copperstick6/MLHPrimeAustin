import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

#checking the Operating system nt = win10
print os.name;

#checking if the newFile.txt file is a file/dir
print "Item exists: " + str(path.exists("newFile.txt"))
print "Item is a file: " + str(path.isfile("newFile.txt"))
print "Item is a file: " + str(path.isdir("newFile.txt"))

#checking the path of the item
print "Item's path: " + str(path.realpath("newFile.txt"))
print "Item's path and name: " + str(path.split(path.realpath("newFile.txt")))

#checking the time it was modified
t = time.ctime(path.getmtime("newFile.txt"))
print "Time modified: " + t
print datetime.datetime.fromtimestamp(path.getmtime("newFile.txt"))

#calculating when the file was last modifed
td = datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("newFile.txt"))
print "It has been " + str(td) + "since the file was last modified"
print "or, " + str(td.total_seconds()) + "seconds"
