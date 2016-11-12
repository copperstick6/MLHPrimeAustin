import xml.dom.minidom
from urllib.request import urlopen


def parseFrom(url_str):
    doc = xml.dom.minidom.parse(urlopen(url_str))
    titles = doc.getElementsByTagName('title')
    startdates = doc.getElementsByTagName('startDate')
    enddates = doc.getElementsByTagName('endDate')
    streets = doc.getElementsByTagName('street')
    cities = doc.getElementsByTagName('street')
    states = doc.getElementsByTagName('street')
    postalcodes = doc.getElementsByTagName('street')
    descriptions = doc.getElementsByTagName('description')
    thelist = []
    for i in range(0, titles.length):
        title = titles[i].firstChild.nodeValue
        startdate = startdates[i].firstChild.nodeValue
        enddate = enddates[i].firstChild.nodeValue
        location = ''
        location += streets[i].firstChild.nodeValue + ' '
        location += cities[i].firstChild.nodeValue + ' '
        location += states[i].firstChild.nodeValue + ' '
        location += postalcodes[i].firstChild.nodeValue
        description = descriptions[i].firstChild
        if description is not None:
            description = description.nodeValue
        thelist.append([title, startdate, enddate, location, description])
    return thelist