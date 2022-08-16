# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymango import mongoClient
#import mongo client to connect
#Creating instance of mongo client
client = MongoClient('mongodb://localhost:27017/')
#Creating database
db = client['cse11']
info =db.cse
student1= {"Reg Num" : "2100030338" , "Name" : "ABCH"},
 {"Reg Num" : "2100030564" , "Name" : "ADRE"},
{"Reg Num" : "210003235" , "Name" : "UGRF"},
#Crreating document
studentdata =db.student
#inserting data
#studentdata.insert_one(student1)
#inserting Many Data
#print