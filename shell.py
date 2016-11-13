#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template
from flask import request
import pymongo
from pymongo import MongoClient
import time
import xmlParser
import googleMapsDistance
app = Flask(__name__)
client = MongoClient()

#oppList is the defined as the current Opportunity List
oppList = xmlParser.parseFrom("https://www.volunteer.gov/footPrintDG.xml")
fullOPS = [[]]
curStreet = "6813 Beverly Glen Drive"
for i in oppList:
    if(googleMapsDistance.getDistance(i[4],curStreet)>100):
        fullOPS.append(i)
#object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addData', methods = ['POST'])
def addingUser():
    request.form



@app.route('/curData', methods = ['POST'])
def returnOpps():
    curStreet = request.form["street"]
    fullOPS = [[]]
    print(curStreet)
    for i in oppList:
        print(i[3])
        if(googleMapsDistance.getDistance(i[3],curStreet)<10000):
            fullOPS.append(i)
    oppList.convert(fullOPS)
    return str(oppList)


if __name__ == "__main__":
    app.run()
