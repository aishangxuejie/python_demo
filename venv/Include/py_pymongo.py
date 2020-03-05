import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
if "two" in dblist:
  print("数据库存在！")
twodb = myclient['two']
collist = twodb.list_collection_names()
# collist = mydb.collection_names()
if "greatLotto" in collist:   # 判断 sites 集合是否存在
  print("集合存在！")

greatLotto = twodb["greatLotto"]
new = greatLotto.find_one()
# print(new)
query_issue_number = {"issue_number":"19045"}
for x in greatLotto.find(query_issue_number,{ "_id": 0, "issue_number": 1, "front_area1": 1, "front_area2": 1, "front_area3": 1, "front_area4": 1 , "front_area5": 1}):
  print(x)