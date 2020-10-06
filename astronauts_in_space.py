# This script will return the amount of people currently in space

import requests

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)
