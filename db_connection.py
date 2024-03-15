import pandas as pd
import pymongo

# MongoDB connection string
url = 'mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority'

# Function to insert data from a CSV file into a MongoDB collection
def insert_data_from_csv(csv_file_path, collection_name):
    # Read CSV file
    df = pd.read_csv(csv_file_path)
    
    # Convert DataFrame to JSON records
    json_records = df.to_dict(orient='records')
    
    # Access the specified collection
    collection = db[collection_name]
    
    # Insert records into the collection, avoiding duplicates based on the "Name" field
    for record in json_records:
        filter_query = {"Name": record["Name"]}
        existing_record = collection.find_one(filter_query)
        if not existing_record:
            collection.insert_one(record)

# Connect to MongoDB
client = pymongo.MongoClient(url)
db = client['WebScrapingData']

# Insert data from CSV files into MongoDB collections
insert_data_from_csv(r"webscraping\data\girls_hostel.csv", "GirlsHostel")
insert_data_from_csv(r"webscraping\data\boys_hostel.csv", "BoysHostel")
insert_data_from_csv(r"webscraping\data\tiffin.csv", "Tiffin")
insert_data_from_csv(r"webscraping\data\pgs.csv", "PgData")

# Close the MongoDB connection
client.close()
