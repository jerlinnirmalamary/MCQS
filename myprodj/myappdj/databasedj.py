from pymongo import MongoClient

client=MongoClient('mongodb://localhost:27017')
db=client.mcq_student
use=db.userlog
q=db.ques
a=db.ans