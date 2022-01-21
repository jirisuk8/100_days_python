
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

# data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
# flight_search = FlightSearch()
#
# if sheet_data[0]["iataCode"] == "":
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     print(f"sheet_data:\n {sheet_data}")
#
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()
flight_search = FlightSearch()
flight_data = FlightData("Prague")
res = flight_data.get_flight_data("Rome")
print(f"Primy let z {res['cityFrom']} do {res['cityTo']} za nejnizsi cenu {res['price']} CZK")
