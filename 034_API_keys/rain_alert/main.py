import requests
from twilio.rest import Client

API_KEY = "0dc2e40d269e61d3f92a12c9c9d5f374"
MY_LAT = -18.737823#50.075539
MY_LONG = 126.148359#14.437800

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "exclude": ["current,minutely,daily,alerts"]
}

with requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=parameters) as response:
    response.raise_for_status()
    weather_data = response.json()

def is_it_going_to_rain(data):
    for hourly_data in data["hourly"][:12]:
        for weather_ids in hourly_data["weather"]:
            if weather_ids["id"] < 700:
                return "Zitra bude prset"

print(is_it_going_to_rain(weather_data))

#### twilio

account_sid = "ACdc740003597924abab7be488463c1acb"
auth_token = "0bba52fc2a5f31c311ce860c197fa61d"

def send_sms(sid, token, text):
    client = Client(sid, token)

    message = client.messages \
                    .create(
                         body=text,
                         from_='+19377497455',
                         to='+420776753420'
                     )

    print(message.sid)

send_sms(account_sid, auth_token, is_it_going_to_rain(weather_data))