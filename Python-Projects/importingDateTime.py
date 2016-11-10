from datetime import date
from datetime import time
from datetime import datetime


#Messing with dates!
#Date is a default package that can be imported with the above
#import statements
def getDate():
    today = date.today()
    print "Today's date is" , today

getDate()

#separating the dates
#please note that you must declare today
def getIndividualDates():
    today = date.today()
    print today.day, today.month, today.year

getIndividualDates()

#getting the time! as well as the date!
def getDateTime():
    today = datetime.now()
    print today

getDateTime()

#getting exclsuively the time!
def getTime():
    today = datetime.time(datetime.now())
    print today
getTime()

#get the day
def getDay():
    allDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.now()
    weekDay = date.weekday(today)
    print "the weekday number is %d" % weekDay
    print "this is a " + allDays[weekDay]

getDay()
