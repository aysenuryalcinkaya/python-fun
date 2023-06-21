import requests
import json


ip_adress='192.168.1.159'

requests_url='https://geolocation-db.com/json/'
response=requests.get(requests_url)
result=response.json()
print(result)
