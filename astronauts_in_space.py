# This script will return the amount of astronauts currently in space.

import requests

data = requests.get('http://api.open-notify.org/astros.json')

json_data = data.json()

amount = json_data['number']
print(f"There are {amount} people in space right now.")

for astros in json_data['people']:
    print(astros['name'])












