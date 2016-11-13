#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template, request, jsonify
import pymongo
from pymongo import MongoClient
import time
import xmlParser
import googleMapsDistance
app = Flask(__name__)
client = MongoClient()


#oppList is the defined as the current Opportunity List

#object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addData', methods = ['POST'])
def addingUser():
    request.form



@app.route('/curData', methods = ['POST'])
def returnOpps():
    oppList = xmlParser.parseFrom("https://www.volunteer.gov/footPrintDG.xml")
    curStreet = str(request.form["street"])
    curStreet = str(curStreet)
    return distanceGetter(curStreet, oppList)

def distanceGetter(curStreet, oppList):
    fullOPS=[]
    for i in oppList:
        if(googleMapsDistance.getDistance(curStreet, i[4])!=0):
            if(googleMapsDistance.getDistance(curStreet, i[4])<10000):
                fullOPS.append(i)
    return jsonify(fullOPS)



if __name__ == "__main__":
    app.run()
