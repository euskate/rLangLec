import requests

# API 요청
response = requests.get('https://api.example.com/data')
data = response.json()

print(data)