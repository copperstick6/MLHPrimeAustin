#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient
import time
import xmlParser
import googleMapsDistance
app = Flask(__name__)
client = MongoClient()

#oppList is the defined as the current Opportunity List
oppList = xmlParser.parseFrom("https://www.volunteer.gov/footPrintDG.xml")

#object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addData', methods = ['POST'])
def addingUser():
    addUserName = str(request.form["username"])
    addPhoneNumber = str(request.form["phonenumber"])
    addAddress = str(request.form["address"])
    return str([addUserName, addPhoneNUmber, addAddress])



@app.route('/curData', methods = ['POST'])
def returnOpps():
    curStreet = str(request.form["street"])
    fullOPS = [[]]
    print(curStreet)
    for i in oppList:
        try:
            googleMapsDistance.getDistance(i[4],curStreet)
        except ValueError:
            continue
    return str(curStreet)


if __name__ == "__main__":
    app.run()
