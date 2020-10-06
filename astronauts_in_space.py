# This script will return the amount of astronauts currently in space.

import requests

data = requests.get('http://api.open-notify.org/astros.json')

json_data = data.json()

amount = json_data['number']
print(f"There are {amount} people in space right now.")

for index, key in enumerate(json_data):
    if index == 1:
        for values in json_data[key]:
            print(values['name'])












