import json
from data_manager import DataManager
from flight_data import FlightData

registration = input("Type 'Y' in you want to register new user or your login email please.\n")

if registration.lower() == "y":
    new_member = DataManager()
    new_member.sign_new_user()
else:
    with open("members.json", 'r') as data_file:
        data = json.load(data_file)
        departure_city = data[registration]["Departure city"]
        destinations = data[registration]["Destinations"]
        if registration.lower() in data:
            user_input = input("Please enter number of destinations you want to add or 'S' in case you want "
                               "to search best deals to your desired destination!\n")
            if user_input.isnumeric():
                for i in range(int(user_input)):
                    destination = input(f"Your destination #{i+1}:\n")
                    data[registration]["Destinations"].append(destination)
                with open("members.json", 'w') as file:
                    json.dump(data, file, indent=4)

            elif user_input.lower() == 's':
                flight_data = FlightData(departure_city, destinations)

                flight_data.send_email()
            else:
                print("Entered input is invalid, please try again!")
        else:
            print("Entered input is invalid, please try again!")



