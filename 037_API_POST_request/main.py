import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "h54f6a5s4f8grgfg45s6df4asd2s1da234weawe54"
USERNAME = "jirka8"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# #------------------- setup user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# #------------------- create graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "my_cycling",
#     "unit": "Km",
#     "type": "float",
#     "color": "sora"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# #------------------- add data to graph
# graph_data_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = datetime.now().strftime("%Y%m%d")
#
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# data_post_config = {
#     "date": today,
#     "quantity": "60.2",
# }

# response = requests.post(url=graph_data_post_endpoint, json=data_post_config, headers=headers)
# print(response.text)

# #------------------- update data in graph
# today = datetime.now().strftime("%Y%m%d")
# date = today
# graph_data_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# data_update_config = {
#     "quantity": "10.2",
# }
# response = requests.put(url=graph_data_update_endpoint, json=data_update_config, headers=headers)
# print(response.text)

# #------------------- delete data in graph

# today = datetime.now().strftime("%Y%m%d")
date = "20220117"
graph_data_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=graph_data_delete_endpoint, headers=headers)
print(response.text)
