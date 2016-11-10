import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

#duplicate a file
if path.exists("newFile.txt"):
    src = path.realpath("newFile.txt")

    #printing the paths etc.
    head,tail = path.split(src)
    print "path: " + head
    print "file: " + tail

    #creating a copy with .bak appended
    dst = src + ".bak"
    shutil.copy(src,dst)

    #copying over all metadata
    shutil.copystat(src, dst)
    root_dir,tail = path.split(src)

    #created a zip file named archive that copies over all files in the directore
    shutil.make_archive("archive", "zip" ,root_dir)

    #created a new zip with the imported ZipFile functions
    #added in specific files
    with ZipFile("testzip.zip","w") as newzip:
        newzip.write("newFile.txt")
        newzip.write("newFile.txt.bak")
#renaming the file
#os.rename("newFile.txt", "textfile.txt")
#os.rename("textfile.txt", "newFile.txt")

print src
