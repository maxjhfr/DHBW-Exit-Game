import requests

url = 'http://192.168.178.63:5000'
data = {'type': 'rfid', 'value': 'scanned'}

response = requests.post(url, json=data)
print(response.json())
