import requests
import os
from datetime import datetime


# ------------- insert workouts as plain text
GENDER = "male"
WEIGHT_KG = 86
HEIGHT_CM = 186
AGE = 29

NUTRIONIX_API_KEY = os.environ["NUTRIONIX_API_KEY"]
NUTRIONIX_API_ID = os.environ["NUTRIONIX_API_ID"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("What was your exercise:\n")

headers = {
    "x-app-id": NUTRIONIX_API_ID,
    "x-app-key": NUTRIONIX_API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint,
                         json=parameters,
                         headers=headers)
result = response.json()
print(result)
# ------------Update google sheet according to exercises performed
google_sheet_endpoint = 'https://api.sheety.co/9dbf30079d02795fe2adfdc99403fd46/workoutTracking/workouts'

SHEETY_AUTHORIZATION = os.environ["SHEETY_AUTHORIZATION"]

sheet_headers = {
    'Content-Type': 'application/json',
    'Authorization': SHEETY_AUTHORIZATION
}

for exercise in result['exercises']:
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    workout = exercise['name'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    sheet_parameters = {
        'workout': {
            "date": date,
            "time": time,
            "exercise": workout,
            "duration": duration,
            "calories": calories
        }
    }

    sheet_response = requests.post(url=google_sheet_endpoint,
                                   json=sheet_parameters,
                                   headers=sheet_headers,
                                   )
    print(sheet_response.json())
