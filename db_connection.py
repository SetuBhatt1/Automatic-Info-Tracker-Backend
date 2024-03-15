import pymongo

url = 'mongodb+srv://bansetu1:bansetu1@cluster0.xkk78vz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = pymongo.MongoClient(url)
db = client['HostelData']
