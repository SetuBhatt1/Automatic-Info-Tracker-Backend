import csv
from django.http import JsonResponse, HttpResponse
from .models import tiffin_collection


def index(request):
    return HttpResponse("<h1>App is running</h1>")


def add_tiffin(request):
    records = {"tiffin_name": "Mom;s Kitchen"}
    tiffin_collection.insert_one(records)
    return HttpResponse("one tiffin service added")


def get_all_tiffins(request):
    tiffins = tiffin_collection.find()
    returns(tiffins)


def get_hostels_data(request):
    hostels_data = []

    # Read the CSV file and load data dynamically
    with open("hostels_data.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            hostels_data.append(row)

    return JsonResponse({"hostels_data": hostels_data})
