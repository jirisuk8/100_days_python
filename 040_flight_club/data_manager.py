import json


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

        # ------------Load google sheet
    # def get_destination_data(self):
    #
    #     sheet_headers = {
    #         'Content-Type': 'application/json',
    #         'Authorization': SHEETY_AUTHORIZATION
    #     }
    #
    #     sheet_response = requests.get(url=sheet_endpoint,
    #                                   headers=sheet_headers)
    #     data = sheet_response.json()
    #     self.destination_data = data['prices']
    #     return self.destination_data

    def sign_new_user(self):
        first_name = input("Welcome to JS Flight Club.\n"
                           "We find the best flight deals and email you.\n"
                           "What is your first name?\n")
        last_name = input("What is your last name?\n")
        while True:
            email = input("What is your email?\n")
            with open("members.json", 'r') as data_file:
                data = json.load(data_file)
                if email not in data:
                    email_check = input("Type your email again please.\n")
                    if email_check == email:
                        break
                    else:
                        print("You typed two different emails! Try again!")
                else:
                    print("Your email is already in database. Try again!")
        departure_city = input("What city do you prefer to start your journey?\n")
        new_data = {
            email: {
                "First name": first_name,
                "Last name": last_name,
                "Departure city": departure_city,
                "Destinations": []
            }
        }

        try:
            with open("members.json", 'r') as data_file:
                data = json.load(data_file)
                print(data)
        except FileNotFoundError:
            with open("members.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("members.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
