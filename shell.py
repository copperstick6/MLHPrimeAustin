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
totOpps=[]
#object posted: ["userName", "PhoneNumber", "address"]
@app.route('/curUser', methods = ['GET'])
def addingUser():
    addUserName = str(request.form["username"])
    addPhoneNumber = str(request.form["phonenumber"])
    addAddress = str(request.form["address"])
    return [addUserName, addPhoneNUmber, addAddress]

@app.route('/curData', methods = ['GET'])
def getOpps():
    return str(totOpps)



@app.route('/appData', methods = ['POST'])
def returnOpps():
    curOpp = str(request.form["opportunity"])
    curDate = str(request.form["date"])
    curLocation = str(request.form["location"])
    curNeeded = str(request.form["needed"])
    totOpps.append([curOpp,curDate,curLocation,curNeeded])
    return str(totOpps)



if __name__ == "__main__":
    app.run()
