from django.http import JsonResponse, HttpResponse
import pymongo
from .models import tiffin_collection
import json
from math import isnan


def get_all_girls_hostel(request):
    url = "mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(url)
    db = client["WebScrapingData"]
    collection = db["GirlsHostel"]

    # Fetch all documents from the collection
    girls_hostels = collection.find()
    girls_hostels_list = list(girls_hostels)

    client.close()

    # Convert ObjectId to string for each document
    for hostel in girls_hostels_list:
        hostel["_id"] = str(hostel["_id"])

    # Return the list of girls' hostels as JSON
    return JsonResponse(girls_hostels_list, safe=False)


# def get_hostels_data(request):
#     hostels_data = []

#     # Read the CSV file and load data dynamically
#     with open("hostels_data.csv", "r", encoding="utf-8") as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             hostels_data.append(row)

#     return JsonResponse({"hostels_data": hostels_data})


def get_all_boys_hostels(request):
    url = "mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(url)
    db = client["WebScrapingData"]
    collection = db["BoysHostel"]

    # Fetch all documents from the collection
    boys_hostels = collection.find()
    boys_hostels_list = list(boys_hostels)

    client.close()

    # Convert ObjectId to string for each document
    for hostel in boys_hostels_list:
        hostel["_id"] = str(hostel["_id"])

    # Return the list of boys' hostels as JSON
    return JsonResponse(boys_hostels_list, safe=False)


def get_all_tiffins(request):
    url = "mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(url)
    db = client["WebScrapingData"]
    collection = db["Tiffin"]

    # Fetch all documents from the collection
    tiffins = collection.find()
    tiffins_list = list(tiffins)

    client.close()

    # Convert ObjectId to string and replace NaN values with null
    for tiffin in tiffins_list:
        tiffin["_id"] = str(tiffin["_id"])
        for key, value in tiffin.items():
            if isinstance(value, float) and isnan(value):
                tiffin[key] = None  # Replace NaN with None

    # Return the list of tiffins as JSON
    return JsonResponse(tiffins_list, safe=False)

def get_all_pgs(request):
    url = "mongodb+srv://mypro7610:setuanu123@cluster0.qwsaugc.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(url)
    db = client["WebScrapingData"]
    collection = db["PgData"]

    # Fetch all documents from the collection
    pgs = collection.find()
    pgs_list = list(pgs)

    client.close()

    # Convert ObjectId to string and replace NaN values with null
    for pg in pgs_list:
        pg["_id"] = str(pg["_id"])
        for key, value in pg.items():
            if isinstance(value, float) and isnan(value):
                pg[key] = None  # Replace NaN with None

    # Return the list of tiffins as JSON
    return JsonResponse(pgs_list, safe=False)

