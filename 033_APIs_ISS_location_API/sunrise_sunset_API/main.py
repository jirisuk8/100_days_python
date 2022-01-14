import requests
from datetime import datetime
import smtplib

MY_LAT = 50.075539
MY_LONG = 14.437800
UTC_ADD_TO_MY_TZ = 1


# ISS position
def get_iss_position():
    with requests.get(url="http://api.open-notify.org/iss-now.json") as response:
        response.raise_for_status()
        data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


# My position
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def get_sunset_sunrise_time():
    with requests.get(url="https://api.sunrise-sunset.org/json", params=parameters) as response:
        response.raise_for_status()
        data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    hour_of_sunrise = int(sunrise.split("T")[1].split(":")[0]) + UTC_ADD_TO_MY_TZ
    hour_of_sunset = int(sunset.split("T")[1].split(":")[0]) + UTC_ADD_TO_MY_TZ
    return hour_of_sunrise, hour_of_sunset


def is_iss_close():
    lat, lng = get_iss_position()
    if abs(lat-MY_LAT) < 5 and abs(lng-MY_LONG)<5:
        return True
    else:
        return False


def is_night():
    sunrise, sunset = get_sunset_sunrise_time()
    hour_now = datetime.now().hour
    if sunset < hour_now or hour_now <= sunrise:
        return True
    else:
        return False


def send_email():
    my_email = "epigeon.cz@gmail.com"
    password = "epigeon.CZ88"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pavelkarel@yahoo.com",
                            msg=f"Subject: Go out and check for ISS!!\n\n Hello,\n"
                                f"The ISS is really close to you, go out and check it")


def send_notification_mail():
    if is_iss_close() and is_night():
        send_email()
    elif not is_night():
        print("Sorry it is not dark outside yet")
    elif not is_iss_close():
        lat, lng = get_iss_position()
        print(f"Sorry the ISS is far from you.\n"
              f"You are at {MY_LAT}, {MY_LONG}. The iss is at {lat}, {lng}")


send_notification_mail()
