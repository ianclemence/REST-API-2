import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 500, "name": "Ian", "views": 10000},
        {"likes": 700, "name": "Joy", "views": 20000},
        {"likes": 980, "name": "Joe", "views": 30000},
        {"likes": 1000, "name": "Bill", "views": 40000}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/6")
print(response.json())


    #FOR UPDATE
#import requests

#BASE = "http://127.0.0.1:5000/"

#response = requests.patch(BASE + "video/2", {"views":99, "likes":101})
#print(response.json())