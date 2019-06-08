import requests
import json

response = requests.get('http://api.ipify.org/?format=json')

print(response.json())
