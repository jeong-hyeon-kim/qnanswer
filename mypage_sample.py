from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbbbackco

db.mypage_sample.insert_one({'id':'id1','question':'q3','answer':'a1','time':'2021년 10월 07일 01시'})
db.mypage_sample.insert_one({'id':'id1','question':'q3','answer':'a2','time':'2021년 10월 07일 02시'})