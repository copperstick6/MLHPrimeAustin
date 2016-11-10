#importing the URL lib package for python 2
import urllib2
#opening the URL
webUrl = urllib2.urlopen("https://www.cs.utexas.edu/~naren/")
#getcode returns the status of the request to the website
print "result code: " + str(webUrl.getcode())
#read() reads the contents of the code on the website
data = webUrl.read()
print data
