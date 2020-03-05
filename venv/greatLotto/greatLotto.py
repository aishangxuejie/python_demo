import pymongo
import json
import numpy as np
from matplotlib import pyplot as plt 

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
twodb = myclient["two"]
greatLotto = twodb["greatLotto"]
json_line = greatLotto.find({"issue_number":{"$gte":"19000"}},{"_id":0,"issue_number":1,"front_area1":1,"front_area2":1,"front_area3":1,"front_area4":1,"front_area5":1,"back_area1":1,"back_area2":1})
issue_number = []
front_area1 = []
front_area2 = []
front_area3 = []
front_area4 = []
front_area5 = []
# print(list(json_line))
for i in json_line :
	issue_number.append(i["issue_number"])
	front_area1.append(i["front_area1"])
	front_area2.append(i["front_area2"])
	front_area3.append(i["front_area3"])
	front_area4.append(i["front_area4"])
	front_area5.append(i["front_area5"])

colors = ['red', 'blue', 'green', 'orange', 'black']

plt.plot(issue_number,front_area1,colors[0])
plt.plot(issue_number,front_area2,colors[1])
plt.plot(issue_number,front_area3,colors[2])
plt.plot(issue_number,front_area4,colors[3])
plt.plot(issue_number,front_area5,colors[4])

plt.grid()  # 生成网格
plt.xlabel("Date",fontsize = 8)
plt.ylabel("Value",fontsize = 8)
plt.title("greatLotto")
plt.show()

# print(issue_number)
# print(front_area1)
# print(front_area2)
# print(front_area3)
# print(front_area4)
# print(front_area5)
