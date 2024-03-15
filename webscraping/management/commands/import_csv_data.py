# from django.core.management.base import BaseCommand
# import csv
# import os
# from db_connection import client, db

# class Command(BaseCommand):
#     help = 'Imports specific CSV data into MongoDB'

#     def handle(self, *args, **options):
#         data_folder = "data" # Assuming your CSV files are in a folder named "data"
#         collection_name = "GirlsHostel" # MongoDB collection name
#         csv_file_name = "girls_hostel.csv" # Specific CSV file name

#         # Full path to the CSV file
#         file_path = os.path.join(data_folder, csv_file_name)
#         data = self.read_csv(file_path)

#         # Filtering logic: keep rows where 'Pincode' is 387001 or 387002
#         def condition(row):
#             return row['Pincode'] in ['387001', '387002']
#         filtered_data = self.filter_data(data, condition)

#         # Store filtered data in MongoDB
#         self.store_in_mongodb(collection_name, filtered_data)

#     def read_csv(self, file_path):
#         data = []
#         with open(file_path, newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 data.append(row)
#         return data

#     def filter_data(self, data, condition):
#         return [row for row in data if condition(row)]

#     def store_in_mongodb(self, collection_name, data):
#         collection = db[collection_name]
#         collection.insert_many(data)
