import urllib2
import json

urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
webUrl = urllib2.urlopen(urlData)
print webUrl.getcode()
if (webUrl.getcode() == 200):
    data = webUrl.read()
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    count = theJSON["metadata"]["count"];
    print str(count) + " events recorded"
    for i in theJSON["features"]:
        print i["properties"]["place"]
    print "\n"
    for i in theJSON["features"]:
        if i["properties"]["mag"]>=4.0:
            print i["properties"]["mag"], i["properties"]["place"]
    print "\n"
    for i in theJSON["features"]:
        if i["properties"]["felt"]>=0:
            print i["properties"]["felt"], i["properties"]["place"]
else:
    print "error!"
