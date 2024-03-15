import pymongo

url = 'mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(url)
db = client['WebScrapingData']
