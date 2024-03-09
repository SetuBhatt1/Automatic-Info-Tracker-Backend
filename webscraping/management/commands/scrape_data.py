# # scrape_data.py
#
# from django.core.management.base import BaseCommand
# import http.client
# import json
# import csv
#
# class Command(BaseCommand):
#     help = 'Fetch data from API and write to CSV file'
#
#     def handle(self, *args, **kwargs):
#         conn = http.client.HTTPSConnection("api.webscrapingapi.com")
#
#         conn.request("GET", "/v1?api_key=KpqEBf1TngqNP887BZvNeENHr3KSJKmk&url=https%3A%2F%2Fwww.justdial.com%2FNadiad%2FHostels%2Fnct-10253730&render_js=1&proxy_type=residential&timeout=30000&country=us")
#
#         res = conn.getresponse()
#         data = res.read()
#
#         # Print the raw data received from the API for debugging
#         print("Raw API Response:", data)
#
#         if not data:
#             print("Empty response received from the API")
#             return
#
#         # Assuming the response is in JSON format
#         try:
#             json_data = json.loads(data.decode("utf-8"))
#         except json.decoder.JSONDecodeError as e:
#             print("Error decoding JSON:", e)
#             return  # Exit the handle method if there's an error decoding JSON
#
#         # Print the parsed JSON data for debugging
#         print("Parsed JSON Data:", json_data)
#
#         # Extract the required information from the JSON response and prepare for CSV
#         hostels = json_data.get('data', {}).get('hostels', [])
#
#         # Define CSV file name
#         csv_filename = 'hostels_data.csv'
#
#         # Write data to CSV
#         with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
#             fieldnames = ['Name', 'Address', 'Phone']
#             writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#             writer.writeheader()
#             for hostel in hostels:
#                 writer.writerow({'Name': hostel.get('name', ''),
#                                  'Address': hostel.get('address', ''),
#                                  'Phone': hostel.get('phone', '')})
#
#         self.stdout.write(self.style.SUCCESS(f"Data has been written to {csv_filename}"))