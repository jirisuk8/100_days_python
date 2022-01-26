import os
import requests
from datetime import datetime, timedelta
import smtplib


TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, departure_city, destinations):
        self.destinations = destinations
        self.departure_city = self.get_destination_code(departure_city)
        self.date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")

    @staticmethod
    def get_destination_code(city_name):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}locations/query",
                                headers=headers,
                                params=parameters)
        return response.json()['locations'][0]["code"]

    def get_flight_data(self, arrival_city):
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {
            "fly_from": self.departure_city,
            "fly_to": self.get_destination_code(arrival_city),
            "date_from": self.date_from,
            "date_to": self.date_to,
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "CZK",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}v2/search",
                                headers=headers,
                                params=parameters)
        try:
            res = response.json()["data"][0]
            return f"Primy let z {res['cityFrom']} do {res['cityTo']} za nejnizsi cenu {res['price']} CZK\n"
        except IndexError:
            return f"Let z {self.departure_city} do {arrival_city} nelze nalezt\n"

    def get_cheapest_flights(self, destinations):
        email_body = ''
        for destination in destinations:
            email_body += self.get_flight_data(destination)
        return email_body

    def send_email(self):
        my_email = "epigeon.cz@gmail.com"
        password = "epigeon.CZ88"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="pavelkarel@yahoo.com",
                                msg=f"Subject: Vysledky hledani letenek JS Flight Club\n\n Dobry den,\n"
                                    f"vysledky vaseho hledani:\n\n "
                                    f"{self.get_cheapest_flights(self.destinations)}")
        print('Email has been sent!')
