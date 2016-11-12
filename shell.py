#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template
from flask import request
import pymongo
from pymongo import MongoClient
import time
import xmlParser
app = Flask(__name__)
client = MongoClient()

#oppList is the defined as the current Opportunity List
oppList = xmlParser.parseFrom("https://www.volunteer.gov/footPrintDG.xml")

#object posted: ["userName", "PhoneNumber", "address"]
@app.route('/addData', methods = ['POST'])
def addingUser():
    request.form



@app.route('/curData', methods = ['GET'])
def returnOpps():
    print(oppList)
    return str(oppList)


if __name__ == "__main__":
    app.run()
