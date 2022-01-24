import os
import requests
from datetime import datetime, timedelta
from flight_search import FlightSearch

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, departure_city):
        self.departure_city = self.get_destination_code(departure_city)
        self.date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}locations/query",
                                headers=headers,
                                params=parameters)
        return response.json()['locations'][0]["code"]