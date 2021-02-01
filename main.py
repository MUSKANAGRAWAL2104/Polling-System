import requests
import asyncio
import json
import random
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
queue=[]
async def main():
    lst = ['https://www.thecocktaildb.com/api/json/v1/1/random.php','https://randomuser.me/api/']
    for i in range(random.randint(1,12)):
        data=requests.get(random.choice(lst))
        queue.append(data.text)
        await asyncio.sleep(random.randint(1,5))
        return
def entry():
    while (True):
        if (len(queue) == 0):
            break
        j = json.loads(queue.pop(0))
        x = mycol.insert_one(j)
        return print("data entry successfully")
while(True):
    lst = [asyncio.run(main()), entry()]
    random.choice(lst)



