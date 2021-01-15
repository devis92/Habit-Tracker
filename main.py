import requests
import datetime as dt
USERNAME = "iqboladahamjonov"
TOKEN = "iqboladahamjonovtoken"
GRAPH_ID = "graph1"

#Create a user account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

#Create a new pixelation graph definition.
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id":GRAPH_ID,
    "name": "PyCodingGraph",
    "unit": "Minutes",
    "type": "int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers )
# print(response.text)

###It records the quantity of the specified date as a "Pixel".###
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.datetime.now()       #(year=2021, month=1, day=12)
pixel_header  = {
    "X-USER-TOKEN": TOKEN
}
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many minutes did spend for coding today? ")
}
response = requests.post(url = pixel_endpoint, json=pixel_params, headers=pixel_header)
print(response.text)

###Update the quantity already registered as a "Pixel"###
update_pixed_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_pixed_params = {
    "quantity" : "360"
}

# response = requests.put(url = update_pixed_endpoint, json=update_pixed_params, headers=pixel_header)
# print(response.text)

###Delete the registered "Pixel"####
delete_pixed_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# response = requests.delete(url = update_pixed_endpoint, headers=pixel_header)
# print(response.text)


