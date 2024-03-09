import csv
from django.http import JsonResponse

def get_hostels_data(request):
    hostels_data = []

    # Read the CSV file and load data dynamically
    with open('hostels_data.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            hostels_data.append(row)

    return JsonResponse({'hostels_data': hostels_data})
