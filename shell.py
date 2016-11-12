#basic shell with data for our project
#data is manually added until further notice
from flask import Flask
from flask import request
import time
app = Flask(__name__)

#oppList is the defined as the current Opportunity List
oppList = [["","","",""]]
curTime = (time.strftime("%d/%m/%Y"))
print(curTime)



@app.route('/addData', methods = ['POST'])
def addingOpps():
    #removing objects that contain times we don't need or want
    for i in oppList:
        if request.form['date'] > curTime:
            newList = [request.form['opportunity'], request.form['curPerson'], request.form['date'], request.form['description']]
            oppList.append(newList)
