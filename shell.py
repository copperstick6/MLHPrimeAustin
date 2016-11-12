#basic shell with data for our project
#data is manually added until further notice
from flask import Flask, render_template
from flask import request
import pymongo
from pymongo import MongoClient
import time
app = Flask(__name__)

#oppList is the defined as the current Opportunity List
oppList = [["dankMemes","0","dankMemes","dankMemes"]]
curTime = (time.strftime("%d/%m/%Y"))
print(curTime)




@app.route('/curData', methods = ['GET'])
def returnOpps():
    print(oppList)
    return str(oppList)


if __name__ == "__main__":
    app.run()
