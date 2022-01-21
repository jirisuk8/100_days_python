import os
import requests
from pprint import pprint

sheet_endpoint = 'https://api.sheety.co/9dbf30079d02795fe2adfdc99403fd46/flightDeals/prices'
SHEETY_AUTHORIZATION = os.environ["SHEETY_AUTHORIZATION"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

        # ------------Load google sheet
    def get_destination_data(self):

        sheet_headers = {
            'Content-Type': 'application/json',
            'Authorization': SHEETY_AUTHORIZATION
        }

        sheet_response = requests.get(url=sheet_endpoint,
                                      headers=sheet_headers)
        data = sheet_response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheet_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)


