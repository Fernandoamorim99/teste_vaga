import requests
import json

url = "http://api.teste.vallions.com.br:7000/api/users"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)


response = response.text.encode('utf8')
response = json.loads(response)
for a in range(0,len(response)):
	print(response[a])