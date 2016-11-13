import xml.dom.minidom
from urllib.request import urlopen


def parseFrom(url_str):
    doc = xml.dom.minidom.parse(urlopen(url_str))
    titles = doc.getElementsByTagName('title')
    startdates = doc.getElementsByTagName('startDate')
    enddates = doc.getElementsByTagName('endDate')
    streets = doc.getElementsByTagName('street')
    cities = doc.getElementsByTagName('city')
    states = doc.getElementsByTagName('state')
    postalcodes = doc.getElementsByTagName('postalCode')
    descriptions = doc.getElementsByTagName('description')
    thelist = []
    for i in range(0, titles.length):
        title = titles[i].firstChild.nodeValue
        startdate = startdates[i].firstChild.nodeValue
        if int(startdate[0:4]) < 2016:
            continue
        enddate = enddates[i].firstChild.nodeValue
        location = ''
        location += streets[i].firstChild.nodeValue + ' '
        location += cities[i].firstChild.nodeValue + ' '
        location += states[i].firstChild.nodeValue + ' '
        location += postalcodes[i].firstChild.nodeValue
        postalCodes = ''
        postalCodes += postalcodes[i].firstChild.nodeValue
        description = descriptions[i].firstChild
        if description is not None:
            description = description.nodeValue
        thelist.append([title, startdate, enddate, location, postalCodes, description])
    return thelist
