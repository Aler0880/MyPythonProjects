# Работа с API (requests, JSON)

import requests

url = "https://api.github.com/repos/python/cpython"

response = requests.get(url)

print(response.status_code)

print(response.text[:500])
