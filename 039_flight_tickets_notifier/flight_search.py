import os
import requests

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query",
                                headers=headers,
                                params=parameters)
        return response.json()['locations'][0]["code"]
