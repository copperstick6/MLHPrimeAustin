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
@app.route('/curData', methods = ['GET'])
def addingUser():
<<<<<<< HEAD
    return str(totOpps)
=======
    addUserName = str(request.form["username"])
    addPhoneNumber = str(request.form["phonenumber"])
    addAddress = str(request.form["address"])
    return [addUserName, addPhoneNUmber, addAddress]
>>>>>>> 9eb36e918793f50fe6470e543789222123c1b609



@app.route('/addData', methods = ['POST'])
def returnOpps():
    totOpps = []
    curOpp = str(request.form["opportunity"])
    curDate = str(request.form["date"])
    curLocation = str(request.form["location"])
    curNeeded = str(request.form["needed"])
    totOpps.append([curOpp,curDate,curLocation,curNeeded])
    return str(totOpps)



if __name__ == "__main__":
    app.run()
